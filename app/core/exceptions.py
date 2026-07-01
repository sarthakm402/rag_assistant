class RAGException(Exception):

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class DocumentNotFound(RAGException):
    pass


class EmbeddingError(RAGException):
    pass


class RetrievalError(RAGException):
    pass


class LLMError(RAGException):
    pass