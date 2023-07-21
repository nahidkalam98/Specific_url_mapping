from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<i>This is my first string</i>')

def second(request):
    return HttpResponse('<i>This is my second string</i>')

