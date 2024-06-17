import pymupdf
import os
import cloudinary
import cloudinary.uploader
import requests
from cloudinary.utils import cloudinary_url
import urllib.parse

class PdfHighlighter:
  def __init__(self, pdf_path, ner_dict):
    self.pdf_path = pdf_path
    self.ner_dict = ner_dict
    self.list = []

  def highlight(self):
    # The cloudinary credential
    cloudinary.config(
        cloud_name='dzlv9zrk8',
        api_key='689549637748837',
        api_secret='8FaQn5CszbftFojnsUnPUN0Z7tM'
    )
    try:
      print("highlighting user pdf.....")

      for val in self.ner_dict.keys():
        self.list.append(val)


      doc = pymupdf.open(self.pdf_path)

      for page in doc:
        for word in list:
            instance = page.search_for(word)
            for inst in instance:
                page.add_highlight_annot(inst)

 


      # Save the modified PDF
      doc.save("..highlighted.pdf")
      doc.close() 



    except Exception as err:
      print(f"Error occured while reading pdf : {err}")
