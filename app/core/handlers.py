from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import RAGException


async def rag_exception_handler(
    request: Request,
    exc: RAGException
):

    return JSONResponse(
        status_code=500,
        content={
            "error": exc.message
        }
    )