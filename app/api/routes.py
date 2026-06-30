from fastapi import APIRouter

from app.api.schemas import QueryRequest, QueryResponse
from app.services.rag_service import RAGService

router = APIRouter()

rag_service = RAGService()


@router.post(
    "/query",
    response_model=QueryResponse
)
def query(
    request: QueryRequest
):

    response = rag_service.ask(
        request.query
    )

    return QueryResponse(
        answer=response["answer"],
        sources=response["sources"]
    )