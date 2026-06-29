from app.retrieval.bm25_retriever import BM25Retriever

retriever = BM25Retriever()

results = retriever.retrieve(
    "machine learning"
)

for chunk, score in results:

    print("=" * 70)

    print(f"Score  : {score:.3f}")
    print(f"Source : {chunk['source']}")
    print(f"Page   : {chunk['page']}")

    print()

    print(chunk["text"][:300])