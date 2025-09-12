from opentelemetry.metrics import CallbackOptions, Observation, set_meter_provider, get_meter, Counter, ObservableGauge, Histogram
from prometheus_client import start_http_server
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import SERVICE_NAME, Resource, SERVICE_INSTANCE_ID
from uuid import uuid4
from config import CONFIG
from typing import Tuple, Dict, Union
from logger import get_logger

logger = get_logger(__name__)

prom_port = CONFIG.prometheus_port

start_http_server(port=prom_port, addr="0.0.0.0")

# This function ensures that a string is ASCII and doesn't exceed a certain length
def _safe_string(s: str, max_length: int = 45) -> str:
    # Ensure the string is ASCII
    if not s.isascii():
        # Remove non-ASCII characters
        s = s.encode("ascii", "ignore").decode()
    # Truncate if longer than max_length
    if len(s) > max_length:
        s = s[:max_length]
    # Replace problematic characters with underscores
    return s.replace("'", "").replace(" ", "_")

# Represents a frozen set of labels.
LabelsTuple = Tuple[Tuple[str, str], ...]
GaugeValue = Union[float, int]

# This class sends metrics that can be scraped by Prometheus
class TelMetrics:
    _instance = None

    def __new__(cls):
        # Implement Singleton pattern, only one instance of this class should exist
        if not cls._instance:
            cls._instance = super(TelMetrics, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Prevents re-initialization if an instance already exists
        if hasattr(self, 'initialized'):
            return

        # Generate a unique Worker UUID for this instance
        self.worker_uuid = str(uuid4())

        # Create a resource with service name and instance ID
        resource = self._get_resource()

        reader = PrometheusMetricReader()

        self.metric_reader = reader

        # Register a MeterProvider with Opentelemetry
        provider = MeterProvider(resource=resource, metric_readers=[reader])
        set_meter_provider(provider)

        # Get a Meter for collecting metrics
        self.meter = get_meter(CONFIG.service_name)

        # Mark this instance as initialised to prevent reinitialisation
        self.initialized = True

        # Initialise dictionaries to store different types of metrics
        self.counters: Dict[str, Counter] = {}
        self.gauges: Dict[str, ObservableGauge] = {}        
        self.gauge_data: Dict[str, Dict[LabelsTuple, GaugeValue]] = {}
        self.histograms: Dict[str, Histogram] = {}

    # Create a resource with the service name and unique worker UUID
    def _get_resource(self):
        return Resource(attributes={
            SERVICE_NAME: CONFIG.service_name,
            SERVICE_INSTANCE_ID: self.worker_uuid,
        })
    
    def send_metric(self, metric: str, count_val: float | int, labels: dict[str, str] | None = None):
        """
        Record a metric value.

        :param metric: Name of the metric
        :param value: Value of the metric
        :param labels: Optional labels for the metric
        """
        try:
            count_val = count_val if count_val >= 0 else 0
            processed_labels = {}

            if labels is not None:
                # Process each key and value in labels with safe_string
                processed_labels = {_safe_string(key): _safe_string(
                    value) for key, value in labels.items()}

            # Process the data and create counters if necessary
            metric = _safe_string(metric)
            counter_key = f"{metric}"

            # If the counter does not exist already, create it
            if counter_key not in self.counters:
                self.counters[counter_key] = self.meter.create_counter(
                    name=counter_key,
                    unit="1",
                    description=f'{metric} counter'
                )

            # Increment the counter with the label (attribute) values
            self.counters[counter_key].add(
                count_val, attributes=processed_labels)

        # Error handling for issues in sending metric data
        except Exception as e:
            logger.error(f"There was an error while sending telemetry data: {e}")

    def record_gauge(self, metric: str, val: float | int, labels: dict[str, str] | None = None):
        """
        Record a gauge metric.

        :param metric: Name of the metric
        :param val: Value of the metric
        :param labels: Optional labels for the metric
        """
        try:
            val = val if val >= 0 else 0
            processed_labels: Dict[str, str] = {}
            if labels is not None:
                # Process each key and value in labels with safe_string
                processed_labels = {_safe_string(key): _safe_string(
                    value) for key, value in labels.items()}

            # Process the data and create gauge if necessary
            metric = _safe_string(metric)
            gauge_name = f"{metric}"

            # If the gauge does not exist already, create it
            if gauge_name not in self.gauges:
                def callback(options: CallbackOptions, name: str = gauge_name):
                    gauge_entries = self.gauge_data.get(name, {})
                    for labels_tuple, value in gauge_entries.items():
                        labels_dict = dict(labels_tuple)
                        yield Observation(value, attributes=labels_dict)

                self.gauges[gauge_name] = self.meter.create_observable_gauge(
                    name=gauge_name,
                    callbacks=[callback],
                    description=f'{metric} gauge',
                )

            # Update the gauge value
            labels_tuple: LabelsTuple = tuple(sorted(processed_labels.items()))
                        
            if gauge_name not in self.gauge_data:
                self.gauge_data[gauge_name] = {}
                        
            self.gauge_data[gauge_name][labels_tuple] = val

        except Exception as e:
            logger.error(f"There was an error while sending gauge telemetry data: {e}")
    
    def record_histogram(self, metric: str, value: float | int, labels: dict[str, str] | None = None):   
        """
        Record a histogram metric.

        :param metric: Name of the metric
        :param value: Value of the metric
        :param labels: Optional labels for the metric
        """
        try:
            value = value if value >= 0 else 0
            processed_labels = {}

            if labels is not None:            
                # Process each key and value in labels with safe_string
                processed_labels = {_safe_string(key): _safe_string(
                    value) for key, value in labels.items()}

            # Process the data and create histograms if necessary
            metric = _safe_string(metric)
            histogram_key = f"{metric}_histogram"

            # If the histogram does not exist already, create it
            if histogram_key not in self.histograms:
                self.histograms[histogram_key] = self.meter.create_histogram(
                    name=histogram_key,
                    unit="1",
                    description=f'{metric} histogram'
                )

            # Record the value with the label (attribute) values
            self.histograms[histogram_key].record(
                value, attributes=processed_labels)

        # Error handling for issues in sending histogram data
        except Exception as e:
            logger.error(f"There was an error while sending histogram telemetry data: {e}")

# Instantiate the metrics sender
telemetry_custom = TelMetrics()