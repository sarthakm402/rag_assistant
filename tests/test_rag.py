from app.generation.rag_pipeline import RAGPipeline

rag = RAGPipeline()

response = rag.ask(
    "What experience does Sarthak have?"
)

print("\nANSWER\n")
print(response["answer"])