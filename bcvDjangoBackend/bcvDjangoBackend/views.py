
from django.http import HttpResponse

def Pdf_highlighter(request):
    return HttpResponse("the component is for PDF highlight" )

def Pdf_summury(request):
    return HttpResponse("the component is for PDF summury" )

def home(request):
    return HttpResponse("this home page" )
