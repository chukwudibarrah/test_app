from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def chukwudi(request):
    return HttpResponse("Hello, Chukwudi")

def moyra(request):
    return HttpResponse("Hello, Moyra")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })