import streamlit as st
import pymupdf

def get_pdf():
    pdf = st.file_uploader("Upload a file", type=["pdf"])
    return pdf

def extract_text(pdf):
    if(pdf != None):
        st.write("Text obtained from parsing the pdf:")
        text=""
        with pymupdf.open(stream=pdf.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
                text += "\n\n"
        st.write(text)


def main():
    st.title("DEMO OF PDF PARSER")
    st.write("Provide a sample pdf")
    pdf = get_pdf()
    extract_text(pdf)


if __name__ == "__main__":
    main()