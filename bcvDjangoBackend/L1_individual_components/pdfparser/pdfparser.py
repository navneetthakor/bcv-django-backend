import pymupdf

class PdfParser:
  def __init__(self, pdfPath):
    self.pdfPath = pdfPath
    self.text = ""

  def readPdf(self):
    try:
      pdf = pymupdf.open(self.pdfPath)
      for page in pdf:
        self.text += page.get_text()
        self.text += "\n-------------------------------------\n\n"
      return self.text
    except Exception as err:
      print(f"Error occured while reading pdf : {err}")

  def printPdf(self):
    print(self.text)