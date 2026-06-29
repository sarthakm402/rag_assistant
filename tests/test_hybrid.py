# from app.retrieval.hybrid_retriever import HybridRetriever

# retriever = HybridRetriever()

# vector_results, bm25_results = retriever.retrieve(
#     "Apache Spark"
# )

# print("VECTOR RESULTS\n")

# for result in vector_results:

#     print("=" * 60)
#     print(result.payload["source"])
#     print(result.payload["page"])
#     print(result.score)

# print("\n\nBM25 RESULTS\n")

# for chunk, score in bm25_results:

#     print("=" * 60)
#     print(chunk["source"])
#     print(chunk["page"])
#     print(score)
from app.retrieval.hybrid_retriever import HybridRetriever

retriever = HybridRetriever()

results = retriever.retrieve(
    "Apache Spark"
)

for result in results:

    print("=" * 60)

    print(result["source"])
    print(result["page"])
    print(result["score"])

    print(result["text"][:200])