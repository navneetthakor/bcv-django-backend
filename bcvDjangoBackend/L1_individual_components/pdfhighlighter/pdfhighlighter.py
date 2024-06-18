import pymupdf
import os
import cloudinary
import cloudinary.uploader
import requests
from cloudinary.utils import cloudinary_url
import urllib.parse
from django.conf import settings

class PdfHighlighter:
  def __init__(self, pdf_path, ner_dict):
    self.pdf_path = pdf_path
    self.ner_dict = ner_dict
    self.list = []

  def highlight(self):
    # The cloudinary credential
    cloudinary.config(
        cloud_name='deziazvyp',
        api_key='115335176222945',
        api_secret='AJDclFmKfBgeaPqfQtbHqd8sgQ'
    )
    try:
      print("\n\n\nhighlighting user pdf.....\n")
      
      self.list = [key for key in self.ner_dict.keys()]
      # print(self.list)

      doc = pymupdf.open(self.pdf_path)
      print(doc,"\n\n\n")

      for page in doc:
        for word in self.list:
            instance = page.search_for(word)
            for inst in instance:
                page.add_highlight_annot(inst)

      
      STATIC_ROOT_PATH = os.path.join(settings.BASE_DIR, settings.STATIC_ROOT)

      highligh_pdf_path = os.path.join(STATIC_ROOT_PATH, '/highlighted.pdf')
      # Save the modified PDF
      print("path for highlight is : ", highligh_pdf_path,"\n\n\n")
      doc.save(highligh_pdf_path)
      doc.close() 

      return highligh_pdf_path
    
    except Exception as err:
      print(f"Error occured while highlighting pdf : {err}")
