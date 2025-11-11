from django.shortcuts import render

# Create your views here.
#------------------File meaning and how to connect Html file with python file----------
#We do not have any Html file so whenver we want do Html code
#create a templates folder => create  html  file in that.

#views.py is main file in which we do all python code. 

#connect Html file or store Html file in views.py.a

#-----------------------Steps or code to store Html file in views.py---------
#1. first import at top : from djang.template import loader
#django.http is library and inside we jave loader which helps
# to store Html file in variable

#2. create a function  and in that pass request.

#3. inside we use get_template() function to store Html filename

#4. use retrun HttpResponse() and render to display Html file on screen.
#render() means display. HttpReponse means when user  do Html code program sends
#request to browser to display the Html program and browser reply
#by using return Httpresponse and excepts to display on screen

#5. call function in url.py. The reason we need to generate link 
#url.py will do for us. Follow following steps to call
#--------------------------Steps to call function ------------------
#1. from appname.views import functiion
#2. path(" ", functioname)

#---------------------------------------------------------------------
from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())