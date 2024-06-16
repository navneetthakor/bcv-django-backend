from pdfhighlighter import PdfHighlighter

# Instantiating an NER instance of  Ner class
pdfHighlighterInstance = PdfHighlighter("pdfPath", "ner_entities")

# NER main function for making entity relations
pdfHighlighterInstance.highlight()