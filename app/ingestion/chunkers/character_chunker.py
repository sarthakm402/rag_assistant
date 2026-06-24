import uuid
from app.ingestion.chunkers.base_chunker import BaseChunker


class CharacterChunker(BaseChunker):

    def __init__(self, chunk_size=500, overlap=100):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, pages: list[dict]) -> list[dict]:
        """
        Split pages into overlapping character chunks.
        """

        chunks = []

        for page in pages:
            text = page["text"]
            page_num = page["page"]

            start = 0

            while start < len(text):

                end = start + self.chunk_size
                chunk_text = text[start:end]

                chunks.append({
                    "chunk_id": str(uuid.uuid4()),
                    "page": page_num,
                    "text": chunk_text
                })

                start += self.chunk_size - self.overlap

        return chunks