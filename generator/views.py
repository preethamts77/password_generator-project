from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>THE BEAST</h1>')

def eggs(request):
    return HttpResponse('<h1>Eggs are so tasty if cooked good</h1>')
