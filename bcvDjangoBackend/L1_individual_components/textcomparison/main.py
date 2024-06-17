from textcomparison import TextComparison
from textclassifier import TextClassifier
import os
import json
import google.generativeai as genai
from django.conf import settings

STATIC_ROOT_PATH = os.path.join(settings.BASE_DIR, settings.STATIC_ROOT)
pdf_path = os.path.join(STATIC_ROOT_PATH, '/contract.pdf')

# Instantiating an NER instance of  Ner class
classifyInstance1 = TextClassifier(pdfPath_template , ContractType)
classifyInstance2 = TextClassifier(pdf_path , ContractType)

# NER main function for making entity relations
paragraphs_template = classifyInstance1.classify()
paragraphs_contract = classifyInstance2.classify()

# Instantiating an NER instance of  Ner class
comparisonInstance = TextComparison(paragraphs_template ,paragraphs_contract)

dict = comparisonInstance.comparator()
  

# NER method for printing the entities
comparisonInstance.printComparison()
