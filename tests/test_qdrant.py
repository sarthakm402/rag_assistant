from app.vectorstore.qdrant_store import QdrantStore

store = QdrantStore()

store.create_collection(
    vector_size=384
)

print("Collection created")