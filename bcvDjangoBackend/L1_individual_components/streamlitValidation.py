import streamlit as st
import time
from pdfparser.pdfparser import PdfParser
from ner.ner import Ner
from pdfhighlighter.pdfhighlighter import PdfHighlighter

def get_pdf(key):
    pdf = st.file_uploader("Upload a file", type=["pdf"], key=key)
    return pdf

def extract_text(pdf, heading):
    if(pdf != None):
        text=""
        parser_instance = PdfParser(pdf)
        text = parser_instance.readPdf()
        st.write(f"{heading} pdf text :")
        st.write(text)
        return text

def display_entities(entities_dict):
    st.write("Entities recognized:")
    for entity, details in entities_dict.items():
        entity_type = details[0]
        confidence = details[1]
        if entity_type != 'CARDINAL':
            st.write(f"**Entity:** {entity}")
            st.write(f"- **Type:** {entity_type}")
            st.write(f"- **Confidence:** {confidence}")


def highlight(text, textList):
    if text and textList:
        for word in textList:
            highlighted_word = f'<span style="background-color: yellow; color: black;">{word}</span>'
            text = text.replace(word, highlighted_word)
        st.write("Highlighted text:")
        st.markdown(text, unsafe_allow_html=True)
    else:
        st.write("No words to highlight.")

def main():
    st.title("BUSINESS CONTRACT VALIDATION")

    # Pdf Parser

    st.write("Provide a contract")
    pdf1 = get_pdf("key1")
    time_a = time.perf_counter()
    user_pdf = extract_text(pdf1, "Contract")
    time_b = time.perf_counter()

    st.write("Provide a template")
    pdf2 = get_pdf("key2")
    time_c = time.perf_counter()
    template_pdf = extract_text(pdf2, "Template")
    time_d = time.perf_counter()

    if template_pdf:
        st.write("time taken for parsing text : ", ((time_b-time_a) + (time_d-time_c)), " seconds")

    # NER
    time_e = time.perf_counter()
    dict={}
    if user_pdf:
        ner_instance = Ner(user_pdf)
        ner_instance.ner()
        dict = ner_instance.printNER()
        st.write("Entities recognized in User Pdf :")
        display_entities(dict)
    time_f = time.perf_counter()
    st.write("Time taken to perform NER : ", (time_f-time_e), " seconds")

    # Pdf Highlighting
    time_g = time.perf_counter()
    if dict.keys() is not None:
        textList = list(dict.keys())
        highlight(user_pdf, textList)
    time_h = time.perf_counter()
    print("Time taken to highlight pdf :", (time_h - time_g) , " seconds")

    # Text classifier

if __name__ == "__main__":
    main()