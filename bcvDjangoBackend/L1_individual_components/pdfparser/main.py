from pdfparser import PdfParser

# Instantiating  a pdfParser instance of PdfParser class
pdfParserInstance = PdfParser("../../static/download.pdf")

# Read method to read the input pdf.
pdfParserInstance.readPdf()

# Print method to print the text of pdf.
pdfParserInstance.printPdf()