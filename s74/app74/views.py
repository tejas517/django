from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
#5, t, g
def members(request):
    template=loader.get_template("fil.html")
    dict1={
"name":"dhariya"
    }
    return HttpResponse(template.render(dict1, request))
