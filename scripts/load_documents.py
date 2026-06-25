import json

from app.embeddings.embedder import Embedder
from app.vectorstore.qdrant_store import QdrantStore


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

    print("Generating embeddings...")

    embedder = Embedder()

    embeddings = embedder.embed_batch(
        texts
    )

    print(
        f"Generated {len(embeddings)} embeddings"
    )

    store = QdrantStore()

    store.create_collection(
        vector_size=len(embeddings[0])
    )

    print("Uploading to Qdrant...")

    store.insert_batch(
        chunks,
        embeddings
    )

    print("Done")


if __name__ == "__main__":
    main()