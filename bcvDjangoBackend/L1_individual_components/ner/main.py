from ner import Ner

# Instantiating an NER instance of  Ner class
nerInstance = Ner("hlo")

# NER main function for making entity relations
nerInstance.ner()

# NER method for printing the entities
ner_dict = nerInstance.printNER()

print(ner_dict)