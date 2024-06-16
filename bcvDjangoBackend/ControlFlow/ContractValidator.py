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
    
    def classifyText(self, pdfPath, ContractType):
        try:
            classifier = main.TextClassifier(pdfPath,ContractType)
            paragraph = classifier.classify()
            return paragraph
        except Exception as err:
            print(f"Error occured while reading pdf : {err}")

    def compareText(self):
        try:
            textComparison = main.TextComparison(paragraphs_template ,paragraphs_contract)
            dict = textComparison.comparator()
            return dict
        except Exception as err:
            print(f"Error occured while reading pdf : {err}")
