from app.generation.llm import LLM
from app.memory.chat_memory import ChatMemory
from app.retrieval.hybrid_retriever import HybridRetriever
from app.retrieval.reranker import Reranker


class RAGPipeline:

    def __init__(self):

        self.retriever = HybridRetriever()
        self.reranker = Reranker()
        self.llm = LLM()
        self.memory = ChatMemory()

    def ask(
        self,
        query: str,
        top_k: int = 5
    ):

        # Hybrid Retrieval
        results = self.retriever.retrieve(
            query=query,
            top_k=20
        )

        # Rerank
        results = self.reranker.rerank(
            query=query,
            results=results,
            top_k=top_k
        )

        # Conversation History
        history = "\n".join(
            f"{msg['role']}: {msg['content']}"
            for msg in self.memory.get_history()
        )

        # Build Context
        context = "\n\n".join(
            result["text"]
            for result in results
        )

        # Generate Answer
        answer = self.llm.generate(
            query=query,
            context=context,
            history=history
        )

        # Save Conversation
        self.memory.add_user_message(query)
        self.memory.add_assistant_message(answer)

        # Build Sources
        sources = []

        seen = set()

        for result in results:

            source = (
                result["source"],
                result["page"]
            )

            if source not in seen:

                seen.add(source)

                sources.append(
                    {
                        "source": result["source"],
                        "page": result["page"],
                        "score": round(
                            result["rerank_score"],
                            3
                        )
                    }
                )

        return {
            "answer": answer,
            "sources": sources
        }