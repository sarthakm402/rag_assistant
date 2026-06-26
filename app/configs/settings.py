import os
from dataclasses import dataclass


@dataclass
class Settings:
    # Embedding
    embedding_model: str = os.getenv(
        "EMBEDDING_MODEL",
        "BAAI/bge-small-en-v1.5"
    )

    # LLM
    llm_model: str = os.getenv(
        "LLM_MODEL",
        "gemma3:4b"
    )

    # Qdrant
    qdrant_host: str = os.getenv(
        "QDRANT_HOST",
        "localhost"
    )

    qdrant_port: int = int(
        os.getenv("QDRANT_PORT", 6333)
    )

    collection_name: str = os.getenv(
        "COLLECTION_NAME",
        "documents"
    )

    # Retrieval
    top_k: int = int(
        os.getenv("TOP_K", 5)
    )


settings = Settings()