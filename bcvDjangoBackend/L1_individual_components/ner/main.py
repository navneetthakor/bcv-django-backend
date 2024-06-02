from ner import Ner

# Instantiating an NER instance of  Ner class
nerInstance = Ner("text")

# NER main function for making entity relations
nerInstance.ner()

# NER method for printing the entities
nerInstance.printNER()