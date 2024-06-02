
class Ner:
  def __init__(self, pdfText):
    self.text = pdfText

  def ner(self):
    try:
      print("dummy ner method")
    except Exception as err:
      print(f"Error occured while reading pdf : {err}")

  def printNER(self):
    print("dummy ner print method")