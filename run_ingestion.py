import json

from app.ingestion.loaders.pdf_loader import Pdfloader
from app.ingestion.chunkers.character_chunker import CharacterChunker


def main():

    pdf_path =r"/mnt/c/Users/sarthak mohapatra/Downloads/Sarthak_Resume.pdf"
    output_path = "outputs/chunks.json"

    print("Loading PDF...")

    loader = Pdfloader()
    pages = loader.load(pdf_path)

    print(f"Pages loaded: {len(pages)}")

    print("Chunking text...")

    chunker = CharacterChunker(
        chunk_size=500,
        overlap=100
    )

    chunks = chunker.chunk(pages)

    print(f"Chunks created: {len(chunks)}")

    print("Saving chunks...")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()