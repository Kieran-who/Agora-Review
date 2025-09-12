from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Callable
import time

from logger import get_logger

try:
    import weaviate
    from weaviate import WeaviateClient
    from weaviate.auth import AuthApiKey
except ImportError as e:
    raise RuntimeError("weaviate package is required. Install it via `uv pip install weaviate-client`") from e

from config import CONFIG

logger = get_logger(__name__)

@dataclass(frozen=True)
class WeaviateConfig:
    weaviate_version: str
    logging_level: str
    http_host: str
    http_port: int
    http_secure: bool
    grpc_host: str
    grpc_port: int
    grpc_secure: bool
    auth_factory: Callable[[], AuthApiKey]
    connect_timeout_s: float = 5.0
    retries: int = 3
    retry_backoff_s: float = 1.0

    @staticmethod
    def from_app_config() -> "WeaviateConfig":
        return WeaviateConfig(            
            weaviate_version=CONFIG.weaviate.weaviate_version,
            logging_level=CONFIG.logging_level.lower(),
            http_host=CONFIG.weaviate.http_host,
            http_port=CONFIG.weaviate.http_port,
            http_secure=CONFIG.weaviate.http_secure,
            grpc_host=CONFIG.weaviate.grpc_host,
            grpc_port=CONFIG.weaviate.grpc_port,
            grpc_secure=CONFIG.weaviate.grpc_secure,
            auth_factory=CONFIG.weaviate.make_auth,
        )


_client: Optional[WeaviateClient] = None
_client_config: Optional[WeaviateConfig] = None

def _build_client(conf: WeaviateConfig) -> WeaviateClient:
    return weaviate.connect_to_custom(
        http_host=conf.http_host,
        http_port=conf.http_port,
        http_secure=conf.http_secure,
        grpc_host=conf.grpc_host,
        grpc_port=conf.grpc_port,
        grpc_secure=conf.grpc_secure,
        auth_credentials=conf.auth_factory()
    )


def get_weaviate_client(
    force_reconnect: bool = False,
    config: Optional[WeaviateConfig] = None,
) -> WeaviateClient:
    """
    Lazy / cached client accessor.
    Allows injecting a config for tests (e.g. mock endpoints or embedded mode).
    """
    global _client, _client_config

    if _client is not None and not force_reconnect:
        return _client

    if _client is not None and force_reconnect:
        try:
            _client.close()
        except Exception:
            pass
        finally:
            _client = None

    effective_config = config or _client_config or WeaviateConfig.from_app_config()
    _client_config = effective_config

    last_err = None
    for attempt in range(1, effective_config.retries + 1):
        try:
            client = _build_client(effective_config)
            # Light liveness probe (fast); if it fails, close and retry.
            if not client.is_live():
                raise RuntimeError("Weaviate reported not live after connect.")
            _client = client
            logger.debug("Weaviate client established on attempt %d.", attempt)
            return _client
        except Exception as e:
            last_err = e
            logger.warning(
                "Weaviate connection attempt %d/%d failed: %s",
                attempt,
                effective_config.retries,
                e,
            )
            time.sleep(effective_config.retry_backoff_s * attempt)

    raise RuntimeError("Failed to connect to Weaviate after retries.") from last_err


def check_weaviate_connection() -> bool:
    """
    Returns True only if a client exists AND is live.
    Does not create a client (non-intrusive health check).
    """
    if _client is None:
        return False
    try:
        return bool(_client.is_live())
    except Exception:
        return False


def ensure_connection() -> WeaviateClient:
    """
    Ensures a client exists; tries to connect if not present.
    """
    return get_weaviate_client()


def close_weaviate_client():
    global _client
    if _client is not None:
        try:
            _client.close()
        except Exception as e:
            logger.debug("Error closing Weaviate client: %s", e)
        finally:
            _client = None


# Helper for tests to inject a mock/fake.
def set_client_for_tests(fake_client: WeaviateClient):
    global _client
    _client = fake_client

__all__ = [
    "WeaviateConfig",
    "get_weaviate_client",
    "ensure_connection",
    "check_weaviate_connection",
    "close_weaviate_client",
    "set_client_for_tests",
]