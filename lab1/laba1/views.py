from django.shortcuts import render
from django.http import HttpResponse

def homePageView(requests):
    return HttpResponse("Hello, World!")
# Create your views here.
