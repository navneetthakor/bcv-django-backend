
class TextComparison:
  def __init__(self, pdfText, classifiedText):
    self.text = pdfText

  def comparator(self):
    try:
      print("dummy comparator method")
      return "text compared"
    except Exception as err:
      print(f"Error occured while comparing pdf : {err}")

  def printComparison(self):
    print("dummy comparator print method")