import json

from app.embeddings.embedder import Embedder
from app.vectorstore.qdrant_store import QdrantStore
from app.utils.logger import get_logger
logger=get_logger(__name__)

def main():

    with open(
        "outputs/chunks.json",
        "r",
        encoding="utf-8"
    ) as f:
        chunks = json.load(f)

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    logger.info("Generating embeddings...")

    embedder = Embedder()

    embeddings = embedder.embed_batch(
        texts
    )

    logger.info(
        f"Generated {len(embeddings)} embeddings"
    )

    store = QdrantStore()

    store.create_collection(
        vector_size=len(embeddings[0])
    )

    logger.info("Uploading to Qdrant...")

    store.insert_batch(
        chunks,
        embeddings
    )

    logger.info("Done")


if __name__ == "__main__":
    main()