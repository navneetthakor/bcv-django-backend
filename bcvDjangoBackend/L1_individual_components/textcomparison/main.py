from textcomparison import TextComparison

# Instantiating an NER instance of  Ner class
comparisonInstance = TextComparison("text")

# NER main function for making entity relations
comparisonInstance.comparator()

# NER method for printing the entities
comparisonInstance.printComparison()