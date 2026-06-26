from app.retrieval.retriever import Retriever
from app.generation.llm import LLM
from app.retrieval.reranker import Reranker
from app.memory.chat_memory import ChatMemory



class RAGPipeline:

    def __init__(self):
        self.retriever = Retriever(
            embedder=self.embedder,
            vector_store=self.vector_store
        )
        self.reranker = Reranker()
        self.llm = LLM()
        self.memory = ChatMemory()

    def ask(
     self,
     query: str,
     top_k: int = 5
    ):

     results = self.retriever.retrieve(
        query,
        top_k
    )
     history = "\n".join(
    f"{msg['role']}: {msg['content']}"
    for msg in self.memory.get_history()
)
     context = "\n\n".join(
        result.payload["text"]
        for result in results
    )

     answer = self.llm.generate(
        query=query,
        context=context,
        history=history
    )
     self.memory.add_user_message(query)
     self.memory.add_assistant_message(answer)

     sources = []

     seen = set()

     for result in results:

        source = (
            result.payload["source"],
            result.payload["page"]
        )

        if source not in seen:

            seen.add(source)

            sources.append(
                {
                    "source": result.payload["source"],
                    "page": result.payload["page"],
                    "score": round(result.score, 3)
                }
            )
        

     return {
        "answer": answer,
        "sources": sources
    }