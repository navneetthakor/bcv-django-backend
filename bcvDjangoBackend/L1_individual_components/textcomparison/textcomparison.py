
class TextComparison:
  def __init__(self, pdfText):
    self.text = pdfText

  def comparator(self):
    try:
      print("dummy comparator method")
    except Exception as err:
      print(f"Error occured while comparing pdf : {err}")

  def printComparison(self):
    print("dummy comparator print method")