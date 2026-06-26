from app.generation.rag_pipeline import RAGPipeline
rag = RAGPipeline()

response = rag.ask(
    "How much experience does sarthak have"
)

print("\nANSWER\n")
print(response["answer"])

print("\nSOURCES\n")

for source in response["sources"]:

    print(
        f"{source['source']} "
        f"(Page {source['page']}) "
        f"Score={source['score']}"
    )