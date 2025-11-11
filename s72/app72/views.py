from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def members(request):
    template=loader.get_template("index.html")
    student_info={
        "marks":30,
        "subjects":["maths","sceince","english","french"],
        "id":45
    }
    return HttpResponse(template.render(student_info, request))

#----------------------------Assignment--------------------
#1. create a vraiable age. chekc if age is equal to 100 then print you are old else print you are not old.a
#2. create a list of flowers. use for tag in list and print on screen. 
#3. create a list of numbers. use for tag in list. use if tag to chekc if numbers is divisible by 2 tne print even else print odd.a

# do seperate project. 
# properly create a function, inside tat connect with html. create dictonary and inside create age, flower list, number list
# use return httpreponse menas do proper views.py code as well to connect html file with views.print
#use if tag and for tag in index.html
