import json
from pathlib import Path

from app.ingestion.loaders.pdf_loader import Pdfloader
from app.ingestion.chunkers.character_chunker import CharacterChunker
from app.utils.logger import get_logger

logger = get_logger(__name__)


def main():

    data_folder = Path("data")
    output_path = "outputs/chunks.json"

    pdf_files = list(data_folder.glob("*.pdf"))

    if not pdf_files:
        logger.warning("No PDF files found in data/")
        return

    loader = Pdfloader()

    chunker = CharacterChunker(
        chunk_size=500,
        overlap=100
    )

    all_chunks = []

    for pdf_file in pdf_files:

        logger.info(f"Processing {pdf_file.name}")

        pages = loader.load(str(pdf_file))

        logger.info(f"Pages loaded: {len(pages)}")

        chunks = chunker.chunk(pages)

        logger.info(f"Chunks created: {len(chunks)}")

        all_chunks.extend(chunks)

    logger.info(f"Total chunks: {len(all_chunks)}")

    logger.info("Saving chunks...")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(
            all_chunks,
            f,
            indent=2,
            ensure_ascii=False
        )

    logger.info(f"Saved to {output_path}")


if __name__ == "__main__":
    main()