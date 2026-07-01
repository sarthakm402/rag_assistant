from fastapi import APIRouter

from app.api.schemas import QueryRequest, QueryResponse
from app.core.dependencies import get_rag_service

router = APIRouter()


@router.post(
    "/query",
    response_model=QueryResponse
)
def query(
    request: QueryRequest
):

    rag_service = get_rag_service()

    response = rag_service.ask(
        request.query
    )

    return QueryResponse(
        answer=response["answer"],
        sources=response["sources"]
    )