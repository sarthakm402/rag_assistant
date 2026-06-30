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

        pairs = [
            (query, result["text"])
            for result in results
        ]

        scores = self.model.predict(pairs)

        ranked = []

        for result, score in zip(results, scores):

            result["rerank_score"] = float(score)

            ranked.append(result)

        ranked.sort(
            key=lambda x: x["rerank_score"],
            reverse=True
        )

        return ranked[:top_k]