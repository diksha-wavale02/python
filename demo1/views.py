from django.http import HttpResponse
from django.shortcuts import render
def welcome(request):
    return HttpResponse("Welcome coders to Django world")

def bio(request):
    return HttpResponse("<h1> name is diksha </h1>" 
    "<h2> age is 17")

def index(request):
    return HttpResponse("<h1><u>>welcome  to my first html page</u></h1> ")