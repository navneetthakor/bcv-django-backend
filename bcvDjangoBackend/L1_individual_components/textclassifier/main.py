from textclassifier import TextClassifier

# Instantiating an NER instance of  Ner class
classifyInstance = TextClassifier(pdfPath , ContractType)

# NER main function for making entity relations
classifyInstance.classify()

# NER method for printing the entities
classifyInstance.printClassify()
