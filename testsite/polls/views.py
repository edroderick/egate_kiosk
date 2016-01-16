from django.shortcuts import render
from django.http import HttpResponse

def index(reqeust):
    return HttpResponse("Hello, world. Your at the Polls index.")

# Create your views here.
