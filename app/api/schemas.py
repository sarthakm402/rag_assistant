from pydantic import BaseModel


class QueryRequest(BaseModel):
    query: str


class Source(BaseModel):
    source: str
    page: int
    score: float


class QueryResponse(BaseModel):
    answer: str
    sources: list[Source]