from pdfhighlighter import PdfHighlighter

# Instantiating an NER instance of  Ner class
pdfHighlighterInstance = PdfHighlighter("text")

# NER main function for making entity relations
pdfHighlighterInstance.highlight()

# NER method for printing the entities
pdfHighlighterInstance.printHighlight()