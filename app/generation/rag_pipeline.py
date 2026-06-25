from app.retrieval.retriever import Retriever
from app.generation.llm import LLM


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()
        self.llm = LLM()

    def ask(
        self,
        query: str,
        top_k: int = 5
    ):

        results = self.retriever.retrieve(
            query,
            top_k
        )

        context = "\n\n".join(
            result.payload["text"]
            for result in results
        )

        answer = self.llm.generate(
            query=query,
            context=context
        )

        return {
            "answer": answer,
            "sources": results
        }