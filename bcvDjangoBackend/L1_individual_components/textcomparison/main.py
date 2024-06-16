from textcomparison import TextComparison
from textclassifier import TextClassifier
import os
import json
import google.generativeai as genai


# Instantiating an NER instance of  Ner class
classifyInstance1 = TextClassifier(pdfPath_template , ContractType)
classifyInstance2 = TextClassifier(pdfPath_contract , ContractType)

# NER main function for making entity relations
paragraphs_template = classifyInstance1.classify()
paragraphs_contract = classifyInstance2.classify()

# Instantiating an NER instance of  Ner class
comparisonInstance = TextComparison(paragraphs_template ,paragraphs_contract)
  

# NER method for printing the entities
comparisonInstance.printComparison()
