import json

from app.ingestion.loaders.pdf_loader import Pdfloader
from app.ingestion.chunkers.character_chunker import CharacterChunker
from app.utils.logger import get_logger

logger = get_logger(__name__)


def main():

    pdf_path =r"/mnt/c/Users/sarthak mohapatra/Downloads/Sarthak_Resume.pdf"
    output_path = "outputs/chunks.json"

    logger.info("Loading PDF...")

    loader = Pdfloader()
    pages = loader.load(pdf_path)

    logger.info(f"Pages loaded: {len(pages)}")

    logger.info("Chunking text...")

    chunker = CharacterChunker(
        chunk_size=500,
        overlap=100
    )

    chunks = chunker.chunk(pages)

    logger.info(f"Chunks created: {len(chunks)}")

    logger.info("Saving chunks...")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    logger.info(f"Saved to {output_path}")


if __name__ == "__main__":
    main()