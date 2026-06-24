from app.ingestion.loaders.pdf_loader import Pdfloader

loader = Pdfloader()

pages = loader.load(r"/mnt/c/Users/sarthak mohapatra/Downloads/Sarthak_Resume.pdf")

print(f"Pages Loaded: {len(pages)}")

print()

print(pages[0])