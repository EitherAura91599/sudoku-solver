from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainsite(request):
    return HttpResponse("Hello World!")

