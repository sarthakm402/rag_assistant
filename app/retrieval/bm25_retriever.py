import json

from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(
        self,
        chunk_path: str = "outputs/chunks.json"
    ):

        with open(chunk_path, "r", encoding="utf-8") as f:
            self.chunks = json.load(f)

        self.corpus = [
            chunk["text"].split()
            for chunk in self.chunks
        ]

        self.bm25 = BM25Okapi(self.corpus)

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        query_tokens = query.split()

        scores = self.bm25.get_scores(query_tokens)

        scored_chunks = list(
            zip(self.chunks, scores)
        )

        scored_chunks.sort(
            key=lambda x: x[1],
            reverse=True
        )

        results = []

        for chunk, score in scored_chunks[:top_k]:

         results.append(
        {
            "text": chunk["text"],
            "source": chunk["source"],
            "page": chunk["page"],
            "score": float(score),
        }
    )

        return results