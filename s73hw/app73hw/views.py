from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import loader

def members(request):
    template=loader.get_template("index.html")
    student_info={
    'names':"john"    
    }
    return HttpResponse(template.render(student_info, request))
