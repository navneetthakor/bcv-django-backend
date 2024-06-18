from django.shortcuts import render
from django.http import HttpResponse
import os
import cloudinary
import cloudinary.uploader
import requests
from cloudinary.utils import cloudinary_url
import urllib.parse
from django.conf import settings

# for contractify route 
from ControlFlow.main import validatContract
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# The cloudinary credential
cloudinary.config(
    cloud_name='deziazvyp',
    api_key='115335176222945',
    api_secret='AJDclFmKfBgeaPqfQtbHqd8sgQ'
)

# ----------------------------------
# I think this is done by @Ronak in highlighter class so I am marking it more removal 
# ------------------------

# def pdf_highlighter(request):
#      if request.method == 'GET':
#         # Path to the local PDF file
#         file_path = "D:/Ronak/intel project/CUAD_v1/CUAD_v1/full_contract_pdf/Part_I/Affiliate_Agreements/CreditcardscomInc_20070810_S-1_EX-10.33_362297_EX-10.33_Affiliate Agreement.pdf"

#          # Fetching the filename
#         parsed_url = urllib.parse.urlparse(file_path)
#         filename = parsed_url.path.split("/")[-1]

#         try:
#             # Upload the file to Cloudinary with filename
#             result = cloudinary.uploader.upload(file_path, public_id = filename, resource_type="raw")

#             # Get the URL of the uploaded file
#             temp_url = result['secure_url']
#             public_id, options = cloudinary_url(temp_url)
#             return_mess = download_pdf(public_id)
#             return HttpResponse(f"PDF file uploaded and publicly accessible at: <a href='{temp_url}'>{temp_url}</a><br>{return_mess}")
            
#         except Exception as e:
#             return HttpResponse(f"Failed to upload PDF file: {e}")
     
#      return HttpResponse("Send a GET request to upload the PDF file.")


# -----------------
# this is over main route, here I am assuming that 'download_pdf' route gives me
# location of file on local machine, basically path of static folder 
# so that all the classes in validatContract() can access that file 
# -------------------


def contractify(request):
    if request.method == 'POST':
        try:
            # Access raw data
            data = json.loads(request.body)
            inputUrl = data.get('inputUrl')
            templateUrl = data.get('templateUrl')
            agreeType = data.get('agreeType')
            clauses = data.get('clauses')

            # save pdfs 
            inputLocalUrl = download_pdf(inputUrl)
            templateLocalUrl = download_pdf(templateUrl)

            # Process the data
            response_data = validatContract(inputLocalUrl, templateLocalUrl, agreeType, clauses)
            
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


# -------------- 
# route for testing 
# ------------------
def home(request):
    return HttpResponse('I am running')


def download_pdf(public_id):
    try:

        resource_type = 'raw'

        # Creating URL to make request on
        signature = cloudinary_url(public_id, resource_type=resource_type)[0]

        # making request
        response = requests.get(signature, stream=True)

        # Fetching the name of the file
        parsed_url = urllib.parse.urlparse(public_id)
        filename = parsed_url.path.split("/")[-1]
        STATIC_ROOT_PATH = os.path.join(settings.BASE_DIR, settings.STATIC_ROOT)
        path = os.path.join(STATIC_ROOT_PATH, filename)

        if response.status_code == 200:
            # Storing the file locally
            with open(path , 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return "succesfull"

    except requests.exceptions.HTTPError as errh:
        return  f"HTTP Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return  f"Error Connecting: {errc}"
    except requests.exceptions.Timeout as errt:
        return  f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return  f"Something went wrong: {err}"


