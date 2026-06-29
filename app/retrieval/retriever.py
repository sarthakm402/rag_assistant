from app.embeddings.embedder import Embedder
from app.vectorstore.qdrant_store import QdrantStore


class Retriever:

    def __init__(self, embedder:Embedder,
        vector_store:QdrantStore):
        self.embedder = embedder
        self.store =vector_store

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
        formatted_results = []

        for result in results.points:
         formatted_results.append(
        {
            "text": result.payload["text"],
            "source": result.payload["source"],
            "page": result.payload["page"],
            "score": float(result.score),
        }
    )

        return formatted_results