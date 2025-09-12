from weaviate import WeaviateClient
from weaviate.classes.config import Property, DataType
from logger import get_logger

logger = get_logger(__name__)

# Helper to delete collections
def clear_weaviate_records(client: WeaviateClient, collections: list[str]) -> None:
    for col in collections:
        client.collections.delete(col)

def ensure_schema(client: WeaviateClient, clear_data: bool = False):
    # disable auto vectoriser; we will push our own vectors

    # If we are clearing data, we do so by first trying to delete the existing collections
    if clear_data:
        logger.info("Clearing existing data from Weaviate")
        clear_weaviate_records(client, ["PreviousPosts"])

     
    if not client.collections.exists("PreviousPosts"):
        client.collections.create(
            name="PreviousPosts",
            properties=[
                Property(name="published_date", data_type=DataType.DATE),
                Property(name="title", data_type=DataType.TEXT),
                Property(name="summary", data_type=DataType.TEXT),
                Property(name="blog_id", data_type=DataType.TEXT),
            ],
            vector_config=None,
        )
    logger.info("Schema ensured")
