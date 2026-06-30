from app.generation.rag_pipeline import RAGPipeline


class RAGService:

    def __init__(self):
        self.pipeline = RAGPipeline()

    def ask(
        self,
        query: str
    ):
        return self.pipeline.ask(query)