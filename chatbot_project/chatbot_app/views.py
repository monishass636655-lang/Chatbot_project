from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def chatbot(request):
    return HttpResponse("Hello Monisha! This is my chatbot running in Django.")