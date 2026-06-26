from app.retrieval.retriever import Retriever
from app.generation.llm import LLM
from app.retrieval.reranker import Reranker



class RAGPipeline:

    def __init__(self):
        self.retriever = Retriever(
            embedder=self.embedder,
            vector_store=self.vector_store
        )
        self.reranker = Reranker()
        self.llm = LLM()

    def ask(
        self,
        query: str,
        top_k: int = 5
    ):

        results = self.retriever.retrieve(
         query,
         top_k=20
        )

        results = self.reranker.rerank(
         query=query,
         results=results,
         top_k=5
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