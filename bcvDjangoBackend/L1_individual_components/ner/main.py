from ner import Ner

# Instantiating an NER instance of  Ner class
nerInstance = Ner("This agreement holds between Apple INC.  and Samsung INC. for a joint venture for 6 months for a total budget of $2,00,000.")

# NER main function for making entity relations
nerInstance.ner()

# NER method for printing the entities
nerInstance.printNER()