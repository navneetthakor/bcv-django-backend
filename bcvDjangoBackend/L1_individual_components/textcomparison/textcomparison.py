
class TextComparison:
  def __init__(self, paragraph_template, paragraph_contract classifiedText):
    self.paragraph_template = paragraph_template
    self.paragraph_contract = paragraph_contract

  def comparator(self):
    try:
      print("dummy comparator method")
      return "text compared"
    except Exception as err:
      print(f"Error occured while comparing pdf : {err}")

  def printComparison(self):
    print("dummy comparator print method")
