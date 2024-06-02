from L1_individual_components import main

class ContractValidator:
    def __init__(self, pdfUrl):
        self.defultFileUrl = pdfUrl
    
    def parsePdf(self):
        try:
            pdfparser = main.PdfParser(self.defultFileUrl)
            text = pdfparser.readPdf()
            return text
        except Exception as err:
            print(f"Error occured while reading pdf : {err}")
    
    def performNer(self, plainText):
        try:
            ner = main.Ner(plainText)
            nerText = ner.ner()
            return nerText
        except Exception as err:
            print(f"Error occured while performing ner : {err}")
    
    def classifyText(self, plainText, nerText):
        try:
            classifier = main.TextClassifier(plainText,nerText)
            text = classifier.classify()
            return text
        except Exception as err:
            print(f"Error occured while reading pdf : {err}")

    def compareText(self, plainText, classifiedText):
        try:
            textComparison = main.TextComparison(plainText,classifiedText)
            text = textComparison.comparator()
            return text
        except Exception as err:
            print(f"Error occured while reading pdf : {err}")
