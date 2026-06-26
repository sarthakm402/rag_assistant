from sentence_transformers import CrossEncoder
from app.configs.settings import settings

class Reranker:

    def __init__(
        self,
        model_name: str = settings.reranker_model
    ):
        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        query: str,
        results: list,
        top_k: int = 5
    ):
        """
        Re-rank retrieved documents using a cross-encoder.
        """

        pairs = [
            (query, result.payload["text"])
            for result in results
        ]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(results, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [result for result, _ in ranked[:top_k]]