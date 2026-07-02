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
    reranker_model:str=os.getenv(
        "RERANKER_MODEL",
        "cross-encoder/ms-marco-MiniLM-L-6-v2"
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
    redis_host: str = os.getenv(
    "REDIS_HOST",
    "localhost"
)
    redis_port:int=int(os.getenv("REDIS_PORT",6379))
    redis_db:int=int(os.getenv("REDIS_DB",0))


settings = Settings()