# file_upload_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_upload_view, name='file_upload'),
]
