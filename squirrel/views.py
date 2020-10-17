from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel
from django.views.generic import TemplateView, ListView

def index(request):
    return HttpResponse('Home')

def homepage(request):
    return HttpResponse('Homepage')

def mapping(request):
    return HttpResponse('Map')

def sighting(request):
    return HttpResponse('Sightings') 


