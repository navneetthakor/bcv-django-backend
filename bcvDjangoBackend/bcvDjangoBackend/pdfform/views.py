# file_upload_app/views.py

from django.shortcuts import render
from .forms import FileUploadForm
from django.conf import settings
from django.http import HttpResponse
import os

def file_upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            if 'file' in request.FILES:
                uploaded_file = request.FILES['file']
                
                # Read the contents of the uploaded file
                file_content = uploaded_file.read()
                
                # Optionally save the file in a specific directory
                file_path = os.path.join(settings.BASE_DIR, 'pdfform/static/pdfs', uploaded_file.name)
                with open(file_path, 'wb+') as destination:
                    destination.write(file_content)

                # Return the contents of the file as a response (for demonstration purposes)
                return HttpResponse(f'File uploaded successfully. Content length: {len(file_content)} bytes')
            else:
                return HttpResponse('No file uploaded', status=400)
    
            # Do something with the file...
            return render(request, 'file_upload_success.html', {'file_name': pdf.name})
    else:
        form = FileUploadForm()
    return render(request, 'file_upload.html', {'form': form})
