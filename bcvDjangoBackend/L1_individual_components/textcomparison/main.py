from textcomparison import TextComparison
from textclassifier import TextClassifier

# Instantiating an NER instance of  Ner class
classifyInstance = TextClassifier(pdfPath , ContractType)

# NER main function for making entity relations
paragraphs = classifyInstance.classify(pdfType , ContractType)

# Instantiating an NER instance of  Ner class
comparisonInstance = TextComparison(paragraphs)

# NER main function for making entity relations
comparisonInstance.comparator()

# NER method for printing the entities
comparisonInstance.printComparison()
