from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('THE BEAST')

def eggs(request):
    return HttpResponse('<h1>Eggs are so tasty if cooked good</h1>')
