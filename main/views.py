from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # print("This is a home page")
    return HttpResponse("<h1>Welcome to the home page</h1>")

def contact(request):
    return HttpResponse("<p>This is a contact page</p>")
