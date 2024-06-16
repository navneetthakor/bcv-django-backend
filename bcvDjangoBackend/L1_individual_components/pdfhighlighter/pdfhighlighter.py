import pymupdf

class PdfHighlighter:
  def __init__(self, pdf_path, ner_dict):
    self.pdf_path = pdf_path
    self.ner_dict = ner_dict
    self.list = []

  def highlight(self):
    try:
      print("highlighting user pdf.....")

      for val in self.ner_dict.keys():
        self.list.append(val)


      doc = pymupdf.open(self.pdf_path)

      for page in doc:
        for word in list:
            instance = page.search_for(word)
            for inst in instance:
                page.add_highlight_annot(inst)

      # Save the modified PDF
      doc.save("highlighted.pdf")
      doc.close() 



    except Exception as err:
      print(f"Error occured while reading pdf : {err}")
