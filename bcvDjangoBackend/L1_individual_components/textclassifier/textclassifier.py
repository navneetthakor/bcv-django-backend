
class TextClassifier:
  def __init__(self, pdfText):
    self.text = pdfText

  def classify(self):
    try:
      print("dummy text classifier method")
      return "text clssified"
    except Exception as err:
      print(f"Error occured while classifying text : {err}")

  def printClassify(self):
    print("dummy classify print method")
