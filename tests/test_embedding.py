from app.embeddings.embedder import Embedder

embedder = Embedder()

vector = embedder.embed(
    "Apache Spark is a distributed processing engine"
)

print(type(vector))
print(len(vector))
print(vector[:5])