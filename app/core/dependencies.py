from functools import lru_cache

from app.services.rag_service import RAGService


@lru_cache
def get_rag_service():

    return RAGService()