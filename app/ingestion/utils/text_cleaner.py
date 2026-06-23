"""this is for pdf text cleaning"""
import re

class Textcleaner():
 @staticmethod#so we dont need to make object
 def clean_text(pdf_txt:str)->str:
   text = re.sub(r"\s+", " ", pdf_txt)
   text=text.strip()
   return text
 
