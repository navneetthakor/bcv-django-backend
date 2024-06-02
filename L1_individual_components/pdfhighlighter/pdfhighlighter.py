
class PdfHighlighter:
  def __init__(self, pdfText):
    self.text = pdfText

  def highlight(self):
    try:
      print("dummy highlighter method")
    except Exception as err:
      print(f"Error occured while reading pdf : {err}")

  def printHighlight(self):
    print("dummy highlighter print method")