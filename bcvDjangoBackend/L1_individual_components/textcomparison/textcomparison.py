# from textclassifier.textclassifier import TextClassifier
import os
import json
import google.generativeai as genai

class TextComparison:   
        
  def __init__(self , paragraphs_template ,paragraphs_contract):
    self.pairs = []
    self.paragraphs_template = paragraphs_template
    self.paragraphs_contract = paragraphs_contract
    self.dict = ()
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
      # print(result.text)
      return result.text
    except Exception as err:
      print(f"Error occured while comparing pdf : {err}")

  def comparator(self):
    dict_heading = []
    dict_text = []

    for heading, paragraph in self.paragraphs_contract.items():
       if heading in self.paragraphs_template:
          result = self.individual_comparator(self.paragraphs_template[heading] , paragraph )
          dict_heading.append(heading)
          dict_text.append(result)
       else :
          print("heading is missing \n The heading is not present in the provided template or old contract\n\n")
          

    #directly adding key-pair value to dictinary was not working , so alternative approach of using list then converting it into the dict

    temp_dict = dict(zip(dict_heading, dict_text))
    for key, value in temp_dict.items():
      print(f"Key: {key}, Value: {value}")

    # and the dict was not hashable which was require by the control flow contractvalidatior.py file function , hence changed the dict to tuple which is hashable
    self.dict = tuple(temp_dict.items())

    return self.dict
      

  def printComparison(self):
    print("dummy comparator print method")
    for in_data in self.dict:
       print(in_data)
