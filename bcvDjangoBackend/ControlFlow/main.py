from ContractValidator import ContractValidator

def validatContract(inputPdf, templatePdf,agreeType, clauses):

    try:

        # creating model 
        model = ContractValidator(inputPdf, templatePdf, agreeType)

        # parsing pdfs 
        inputText = model.parseInputPdf()
        templateText = model.parseTemplatePdf()

        # ner for input pdf 
        inputpdfNer = model.performNer(inputText)

        # classify text 
        inputClassifiedText = model.classifyInputText()
        templateClassifiedText = model.classifyTemplateText()

        # compare classified text 
        compare_dic = model.compareText(inputClassifiedText, templateClassifiedText)

        # highligh pdf 
        highlitedPdf = model.highlightPdf(inputpdfNer)

        # summary of pdf 


        # returning output
        return {compare_dic, highlitedPdf}

    except Exception as err:
        print("error occured in main function")
        raise Exception(f"error: {err}")





