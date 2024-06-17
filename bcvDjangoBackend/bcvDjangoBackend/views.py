from django.shortcuts import render
from django.http import HttpResponse
import os
import cloudinary
import cloudinary.uploader
import requests
from cloudinary.utils import cloudinary_url
import urllib.parse
from django.conf import settings

# The cloudinary credential
cloudinary.config(
    cloud_name='dzlv9zrk8',
    api_key='689549637748837',
    api_secret='8FaQn5CszbftFojnsUnPUN0Z7tM'
)

def pdf_highlighter(request):
     if request.method == 'GET':
        # Path to the local PDF file
        file_path = "D:/Ronak/intel project/CUAD_v1/CUAD_v1/full_contract_pdf/Part_I/Affiliate_Agreements/CreditcardscomInc_20070810_S-1_EX-10.33_362297_EX-10.33_Affiliate Agreement.pdf"

         # Fetching the filename
        parsed_url = urllib.parse.urlparse(file_path)
        filename = parsed_url.path.split("/")[-1]

        try:
            # Upload the file to Cloudinary with filename
            result = cloudinary.uploader.upload(file_path, public_id = filename, resource_type="raw")

            # Get the URL of the uploaded file
            temp_url = result['secure_url']
            public_id, options = cloudinary_url(temp_url)
            return_mess = download_pdf(public_id)
            return HttpResponse(f"PDF file uploaded and publicly accessible at: <a href='{temp_url}'>{temp_url}</a><br>{return_mess}")
            
        except Exception as e:
            return HttpResponse(f"Failed to upload PDF file: {e}")
     
     return HttpResponse("Send a GET request to upload the PDF file.")

def pdf_summury(request):
    return HttpResponse("the component is for PDF summury" )

def home(request):
    return HttpResponse()


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


