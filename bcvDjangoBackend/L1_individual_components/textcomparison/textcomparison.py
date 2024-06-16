
class TextComparison:   
   # Function to add pairs
  def add_pair(template_text, contract_text, output):
      pair = {
          "template_text": template_text,
          "contract_text": contract_text,
          "output": output
      }
      pairs.append(pair)
    
  def __init__(self):
    self.pairs = []
    self. result = ""
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
      
    model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    # List to store pairs
    temp = []
      
    # Load the JSON file
    with open('pairs.json', 'r') as f:
        temp = json.load(f)
  
    # Loop through each entry in the JSON data and add pairs
    for entry in temp:
        template_text = entry["template_text"]
        contract_text = entry["contract_text"]
        output = entry["output"]
        add_pair(template_text, contract_text, output)
    

  def comparator(template_text , contract_text):
    try:
      add_pair(template_text , contract_text, "")
      
      # Concatenate all input-output pairs into a single string
      combined_input = ""
      for pair in pairs[:-1]:
          combined_input += f"input: \"template text\" : \"{pair['template_text']}\"\n\n\"contract text\" : \"{pair['contract_text']}\"\n\nquery : find the difference in contract text in the context of the template text\nand provide it in brief\noutput: {pair['output']}\n\n"
      
      # Add the last pair without the output
      last_pair = pairs[-1]
      combined_input += f"input: \"template text\" : \"{last_pair['template_text']}\"\n\n\"contract text\" : \"{last_pair['contract_text']}\"\n\nquery : find the difference in contract text in the context of the template text\nand provide it in brief"
      
      # Generate content for the last pair using the combined input
      result = model.generate_content([combined_input])
      
      
      print("dummy comparator method")
      return result.text
    except Exception as err:
      print(f"Error occured while comparing pdf : {err}")

  def printComparison(self):
    print("dummy comparator print method")
    print(result.text)
