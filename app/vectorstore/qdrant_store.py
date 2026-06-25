from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)


class QdrantStore:

    def __init__(
        self,
        collection_name: str = "documents"
    ):
        self.collection_name = collection_name

        self.client = QdrantClient(
            host="localhost",
            port=6333
        )

    def create_collection(
        self,
        vector_size: int
    ):

        collections = self.client.get_collections()

        existing = [
            c.name
            for c in collections.collections
        ]

        if self.collection_name in existing:
            return

        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )

    def insert(
        self,
        point_id: int,
        vector: list[float],
        payload: dict
    ):

        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                PointStruct(
                    id=point_id,
                    vector=vector,
                    payload=payload
                )
            ]
        )
    def insert_batch(
     self,
     chunks: list[dict],
     embeddings: list[list[float]]
):

     points = []

     for idx, (chunk, embedding) in enumerate(
        zip(chunks, embeddings)
    ):

        points.append(
            PointStruct(
                id=idx,
                vector=embedding,
                payload={
                    "page": chunk["page"],
                    "text": chunk["text"]
                }
            )
        )

     self.client.upsert(
        collection_name=self.collection_name,
        points=points
    )