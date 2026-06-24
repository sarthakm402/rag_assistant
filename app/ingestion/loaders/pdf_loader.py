import fitz
from app.ingestion.utils.text_cleaner import Textcleaner

class Pdfloader:
    def load(self,pdf_path)->list[dict]:
        doc=fitz.open(pdf_path)
        pages=[]
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            text = Textcleaner.clean_text(text)
            pages.append(
                {
                    "page": page_num + 1,
                    "text": text
                }
            )

        doc.close()
        return pages


