from app.retrieval.retriever import Retriever

retriever = Retriever()
results = retriever.retrieve("Who is Sarthak Mohapatra")

for result in results:
    print("=" * 50)
    print(result.payload["text"][:300])
    print(f"Score: {result.score}")