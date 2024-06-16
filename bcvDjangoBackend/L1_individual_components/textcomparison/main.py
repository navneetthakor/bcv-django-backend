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
comparisonInstance = TextComparison()

template_headning = []
contract_headning = []
template_text = []
contract_text = []

# NER main function for making entity relations

for heading, paragraph in paragraphs_template.items():
    template_headning.append(heading)
    template_headning.append(heading)
  
count = 0

for heading, paragraph in paragraphs_contract.items():
  if heading in template_headning :
    comparisonInstance.comparator(template_text[count] , paragraph )
  count = count + 1
    
  

# NER method for printing the entities
comparisonInstance.printComparison()
