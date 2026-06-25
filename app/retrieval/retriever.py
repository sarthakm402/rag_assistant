from app.embeddings.embedder import Embedder
from app.vectorstore.qdrant_store import QdrantStore


class Retriever:

    def __init__(self):
        self.embedder = Embedder()
        self.store = QdrantStore()

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        query_embedding = self.embedder.embed(query)

        results = self.store.client.query_points(
            collection_name=self.store.collection_name,
            query=query_embedding,
            limit=top_k
        )
        return results.points