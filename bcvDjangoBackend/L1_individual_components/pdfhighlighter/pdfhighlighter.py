import pymupdf
import os
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from django.conf import settings

class PdfHighlighter:
    def __init__(self, pdf_path, ner_dict):
        self.pdf_path = pdf_path
        self.ner_dict = ner_dict
        self.list = []

    def highlight(self):
        try:
            print("\n\n\nhighlighting user pdf.....\n")
            
            self.list = [key for key in self.ner_dict.keys()]
            # print(self.list)

            doc = pymupdf.open(self.pdf_path)
            print(doc,"\n\n\n")

            for page in doc:
                for word in self.list:
                    instance = page.search_for(word)
                    for inst in instance:
                        page.add_highlight_annot(inst)

            # STATIC_ROOT_PATH = os.path.join(settings.BASE_DIR, settings.STATIC_ROOT)

            highligh_pdf_path = os.path.join('./', 'highlighted.pdf')
            # Save the modified PDF
            print("path for highlight is : ", highligh_pdf_path,"\n\n\n")

            doc.save(highligh_pdf_path)
            doc.close() 

            # Upload the file to Cloudinary with filename
            cloudinary.config(
                cloud_name='dzlv9zrk8',
                api_key='689549637748837',
                api_secret='8FaQn5CszbftFojnsUnPUN0Z7tM'
            )

            result = cloudinary.uploader.upload(highligh_pdf_path, public_id='highlighted.pdf', resource_type="raw")

            # Get the URL of the uploaded file
            temp_url = result['secure_url']
            public_id , options = cloudinary_url(temp_url)
            print(public_id)

            os.remove(highligh_pdf_path)

            return public_id

        except Exception as err:
            print(f"Error occurred while highlighting pdf : {err}")

