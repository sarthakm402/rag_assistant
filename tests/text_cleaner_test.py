from app.ingestion.utils.text_cleaner import Textcleaner

sample = """

Hello


World


Apache      Spark

"""

print(Textcleaner.clean_text(sample))