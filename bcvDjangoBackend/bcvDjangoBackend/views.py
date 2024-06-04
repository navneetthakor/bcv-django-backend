from django.shortcuts import render
from django.http import HttpResponse
import os
import cloudinary
import cloudinary.uploader
import requests
from cloudinary.utils import cloudinary_url



cloudinary.config(
    cloud_name='dzlv9zrk8',
    api_key='689549637748837',
    api_secret='8FaQn5CszbftFojnsUnPUN0Z7tM'
)


def pdf_highlighter(request):
     if request.method == 'GET':
        # Path to the local PDF file
        file_path = "D:/Ronak/books/knowledge_book/ArtOfWar.pdf"

        try:
            # Upload the file to Cloudinary
            result = cloudinary.uploader.upload(file_path, resource_type="raw")

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
    return render(request , 'index.html')


def download_pdf(public_id):
    file_name = "test.pdf"

    try:

        resource_type = 'raw'
        signature = cloudinary_url(public_id, resource_type=resource_type)[0]

        response = requests.get(signature, stream=True)

        if response.status_code == 200:
            with open('D:/Ronak/intel_back_end_django/bcv_backend/static/my_downloaded_file.pdf', 'wb') as f:
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

