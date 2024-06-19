# from textclassifier.textclassifier import TextClassifier
import os
import json
import google.generativeai as genai

class TextComparison:   
        
  def __init__(self , paragraphs_template ,paragraphs_contract):
    self.pairs = []
    self.paragraphs_template = paragraphs_template
    self.paragraphs_contract = paragraphs_contract
    self.dict = {}
    self.model = None
   
    genai.configure(api_key="AIzaSyABsR-Bcf2G2jnuwMIhGB0E2L-AlQkUdVE")

      # Create the model
      # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 64,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
      }
      
    self.model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    # List to store pairs
    temp = []
      
    # Load the JSON file
    with open('./L1_individual_components/textcomparison/pairs.json', 'r') as f:
        temp = json.load(f)
  
    # Loop through each entry in the JSON data and add pairs
    for entry in temp:
        template_text = entry["template_text"]
        contract_text = entry["contract_text"]
        output = entry["output"]
        pair = {
          "template_text": template_text,
          "contract_text": contract_text,
          "output": output
        }
        self.pairs.append(pair)
    

  def individual_comparator(self , template_text , contract_text):
    try:
      # Concatenate all input-output pairs into a single string
      combined_input = ""
      for pair in self.pairs[:-1]:
          combined_input += f"input: \"template text\" : \"{pair['template_text']}\"\n\n\"contract text\" : \"{pair['contract_text']}\"\n\nquery : find the difference in contract text in the context of the template text\nand provide it in brief\noutput: {pair['output']}\n\n"
      
      combined_input += f"input: \"template text\" : \"{template_text}\"\n\n\"contract text\" : \"{contract_text}\"\n\nquery : find the difference in contract text in the context of the template text\nand provide it in brief"
      
      # Generate content for the last pair using the combined input
      result = self.model.generate_content([combined_input])
      
      
      print("dummy comparator method")
      return result.text
    except Exception as err:
      print(f"Error occured while comparing pdf : {err}")

  def comparator(self):
    template_headning = []
    contract_headning = []
    template_text = []
    contract_text = []

    # NER main function for making entity relations

    for heading, paragraph in self.paragraphs_template.items():
        template_headning.append(heading)
        template_text.append(paragraph)
  
    count = 0
   
    for heading, paragraph in self.paragraphs_contract.items():
      if heading in template_headning :
        result = self.individual_comparator(template_text[count] , paragraph )
        self.dict[heading] = result
      count = count + 1

    return self.dict
      

  def printComparison(self):
    print("dummy comparator print method")
    print(self.dict)
