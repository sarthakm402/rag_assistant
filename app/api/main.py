from fastapi import FastAPI

from app.api.routes import router
from app.core.exceptions import RAGException
from app.core.handlers import rag_exception_handler


app = FastAPI(
    title="Production RAG API",
    version="1.0.0"
)

app.include_router(router)
app.add_exception_handler(
    RAGException,
    rag_exception_handler
)
