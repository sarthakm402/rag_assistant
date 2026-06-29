from app.embeddings.embedder import Embedder
from app.retrieval.bm25_retriever import BM25Retriever
from app.retrieval.retriever import Retriever
from app.vectorstore.qdrant_store import QdrantStore


class HybridRetriever:

    def __init__(self):

        embedder = Embedder()
        vector_store = QdrantStore()

        self.vector = Retriever(
            embedder=embedder,
            vector_store=vector_store
        )

        self.bm25 = BM25Retriever()

        # Standard RRF constant
        self.rrf_k = 60

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        # Retrieve more candidates from each retriever
        vector_results = self.vector.retrieve(
            query=query,
            top_k=top_k * 2
        )

        bm25_results = self.bm25.retrieve(
            query=query,
            top_k=top_k * 2
        )

        fused_results = {}

        # ----------------------------
        # Vector Search Contribution
        # ----------------------------
        for rank, result in enumerate(vector_results):

            key = (
                result["source"],
                result["page"],
                result["text"]
            )

            if key not in fused_results:

                fused_results[key] = {
                    **result,
                    "fusion_score": 0.0
                }

            fused_results[key]["fusion_score"] += (
                1 / (self.rrf_k + rank + 1)
            )

        # ----------------------------
        # BM25 Contribution
        # ----------------------------
        for rank, result in enumerate(bm25_results):

            key = (
                result["source"],
                result["page"],
                result["text"]
            )

            if key not in fused_results:

                fused_results[key] = {
                    **result,
                    "fusion_score": 0.0
                }

            fused_results[key]["fusion_score"] += (
                1 / (self.rrf_k + rank + 1)
            )

        final_results = sorted(
            fused_results.values(),
            key=lambda x: x["fusion_score"],
            reverse=True
        )

        return final_results[:top_k]