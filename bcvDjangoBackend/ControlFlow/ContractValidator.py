from L1_individual_components import main

class ContractValidator:
    def __init__(self, pdfUrl):
        self.defultFileUrl = pdfUrl
    
    def parsePdf(self):
        try:
            pdfparser = main.PdfParser(self.defultFileUrl)
            pdfparser.readPdf()
            text =  pdfparser.printPdf()
            return text
        except Exception as err:
            print(f"Error occured while reading pdf : {err}")