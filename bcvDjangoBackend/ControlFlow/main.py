import sys
import os

from ControlFlow.ContractValidator import ContractValidator

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../L1_individual_components/')))

def validatContract(inputPdf, templatePdf,agreeType, clauses):

    try:

        # creating model 
        model = ContractValidator(inputPdf, templatePdf, agreeType)

        # parsing pdfs 
        inputText = model.parseInputPdf()
        templateText = model.parseTemplatePdf()

        # ner for input pdf 
        inputPdfNer = model.performNer(inputText)

        # highligh pdf 
        highlitedPdf = model.highlightPdf(inputPdfNer)
        
        # classify text 
        inputClassifiedText = model.classifyInputText()
        templateClassifiedText = model.classifyTemplateText()

        # compare classified text 
        compare_dic = model.compareText(inputClassifiedText, templateClassifiedText)


        # summary of pdf 
        summary = model.getSummary(inputPdfNer, inputText)

        # returning output
        return {compare_dic, highlitedPdf, summary}

    except Exception as err:
        print("error occured in main function")
        raise Exception(f"error: {err}")



if __name__ == "__main__":
    validatContract()

