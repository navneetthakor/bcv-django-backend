
from django.http import HttpResponse

def pdf_highlighter(request):
    return HttpResponse("the component is for PDF highlight" )

def pdf_summary(request):
    return HttpResponse("the component is for PDF summury" )
