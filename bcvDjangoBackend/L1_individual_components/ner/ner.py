from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("flair/ner-english-ontonotes-large")

class Ner:
  def __init__(self, pdfText):
    self.text = pdfText
    self.sentence = ""

  def ner(self):
    try:
      print("Starting NER Task.....")

      self.sentence = Sentence(self.text)

      tagger.predict(self.sentence)

      return {}
    except Exception as err:
      print(f"Error occured while reading pdf : {err}")

  def printNER(self):
    
    print('The following NER tags are found:')
      
    # iterate over entities and print
    for entity in self.sentence.get_spans('ner'):
      print(entity)