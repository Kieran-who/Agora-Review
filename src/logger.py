import logging
import os
from config import CONFIG

def get_logger(name: str = __name__) -> logging.Logger:
    """Create a logger based on the configuration.

    Args:
        name (str): Name of the logger. Defaults to the module's name.

    Returns:
        logging.Logger: Configured logger instance.

    """
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        log_level = CONFIG.logging_level
        logger.setLevel(getattr(logging, log_level, logging.INFO))

        log_format = os.getenv(
            "LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        formatter = logging.Formatter(log_format)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        logger.propagate = False

    return logger