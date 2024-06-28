import streamlit as st
import pymupdf
from ner import Ner

def get_pdf():
    pdf = st.file_uploader("Upload a file", type=["pdf"])
    return pdf

def extract_text(pdf):
    if pdf is not None:
        text = ""
        with pymupdf.open(stream=pdf.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
                text += "\n\n"
        return text
    return ""

def main():
    st.write("DEMO Name Entitiy Reecognition (NER)")
    st.write("Upload a pdf to extract entities")
    pdf=get_pdf()
    if pdf is not None:
        text = extract_text(pdf)
        if text:
            ner_instance = Ner(text)
            ner_instance.ner()
            dict = ner_instance.printNER()
            st.write("Entities recognized :")
            st.write(dict)

if __name__ == "__main__":
    main()