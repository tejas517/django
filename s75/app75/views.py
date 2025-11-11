from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
#5, t, g
def members(request):
    template=loader.get_template("blogpage.html")

    return HttpResponse(template.render())