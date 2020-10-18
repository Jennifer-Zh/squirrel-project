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

def map(request):
    squirrels  = Squirrel.objects.all()[:100]
    context = {
       'squirrels' : squirrels,
       }
    return render(request, 'map.html', context) 

def sighting(request):
    return HttpResponse('Sightings') 


