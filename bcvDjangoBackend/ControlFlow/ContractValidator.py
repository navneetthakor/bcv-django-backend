from L1_individual_components import main

class ContractValidator:
    def __init__(self, inputPdfUrl, templatePdfUrl):
        self.inputPdfUrl = inputPdfUrl
        self.templatePdfUrl = templatePdfUrl
    
    def parsePdfHelper(pdfUrl):
        try:
            pdfparser = main.PdfParser(pdfUrl)
            text = pdfparser.readPdf()
            return text
        except Exception as err:
            print(f"Error occured while reading pdf : {err}")
            return 'error'

    def parseTemplatePdf(self):
        try:
            txt = self.parsePdfHelper(self.templatePdfUrl)
            return txt
        except Exception as err:
            print(f"Error occured while parsing template pdf : {err}")
            return 'error'
        
    def parseInputPdf(self):
        try:
            txt = self.parsePdfHelper(self.inputPdfUrl)
            return txt
        except Exception as err:
            print(f"Error occured while parsing input pdf : {err}")
            return 'error'
    
    def performNer(self, plainText):
        try:
            ner = main.Ner(plainText)
            nerText = ner.ner()
            return nerText
        except Exception as err:
            print(f"Error occured while performing ner : {err}")
            return 'error'
    
    def classifyText(self, pdfPath, ContractType):
        try:
            classifier = main.TextClassifier(pdfPath,ContractType)
            paragraph = classifier.classify()
            return paragraph
        except Exception as err:
            print(f"Error occured while reading pdf : {err}")
            return 'error'

    def compareText(self, paragraphs_template, paragraphs_contract):
        try:
            textComparison = main.TextComparison(paragraphs_template ,paragraphs_contract)
            dict = textComparison.comparator()
            return dict
        except Exception as err:
            print(f"Error occured while text comparison: {err}")
            return 'error'
        
    def highlightPdf(self,inputPdfUrl, ner_dict):
        try:
            pdfHigltr = main.PdfHighlighter(inputPdfUrl, ner_dict)
            pdfHigltr.highlight()
            return 'success'
        except Exception as err:
            print(f"Error occured while highlighting pdf : {err}")
            return 'error'

