from sentence_transformers import SentenceTransformer
class Embedder:

    def __init__(
        self,
        model_name: str = "BAAI/bge-small-en-v1.5"
    ):
        self.model = SentenceTransformer(model_name)

    def embed(self, text: str) -> list[float]:
        """
        Generate embedding for one text.
        """

        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()

    def embed_batch(
        self,
        texts: list[str]
    ) -> list[list[float]]:
        """
        Generate embeddings for many texts.
        """

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True
        )

        return embeddings.tolist()