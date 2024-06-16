
class TextClassifier:
  def __init__(self, pdfPath , ContractType):
    self.text = pdfText
    self.type = ContractType

  def Type1_classify(pdf_path, headings):
    # Extract text from the PDF
    text = extract_text(pdf_path)
    lines = text.split('\n')

    paragraphs = {}
    current_heading = None

    for line in lines:
        stripped_line = line.strip()

        # Check if the line is an exact match for any heading
        if stripped_line in headings:
            current_heading = stripped_line
            paragraphs[current_heading] = ""
        elif current_heading:
            paragraphs[current_heading] += line + "\n"

    return paragraphs

  def type2_classify(pdf_path, headings):
    paragraphs = {}
    current_heading = None

    for page_layout in extract_pages(pdf_path):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    if isinstance(text_line, LTTextLine):
                        line_text = text_line.get_text().strip()

                        # Check if the line starts with any heading and is bold
                        if any(line_text.startswith(heading) for heading in headings):
                            bold = any(isinstance(char, LTChar) and 'Bold' in char.fontname for char in text_line)
                            if bold:
                                current_heading = next(heading for heading in headings if line_text.startswith(heading))
                                paragraphs[current_heading] = ""

                        if current_heading:
                            paragraphs[current_heading] += line_text + "\n"

    return paragraphs

  def classify(self):
    try:
      type1 = ['Beta Test AgreeMent' , 'Influencer Agreement',]
      type2 = ['Default' , 'Franchise Agreement' , 'Joint Venture Agreement' , 'License Agreement']

      with open('./BusinessContractValidation.templates.json') as f:
        data = json.load(f)

      heading = []

      for i in data:
        if i['agreeType'] == ContractType :
          for clause in i['clauses']:
            heading.append(clause)

      if type in type1 :
        paragraphs = Type1_classify(pdfPath, heading)
      else :
        paragraphs = type2_classify(pdfPath, heading)
        
        
      print("dummy text classifier method")
      return "text clssified"
    except Exception as err:
      print(f"Error occured while classifying text : {err}")

  def printClassify(self):
    print("dummy classify print method")
