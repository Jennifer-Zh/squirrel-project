from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Squirrel
from django.views.generic import TemplateView, ListView
from .forms import Form 

def index(request):
    squirrels  = Squirrel.objects.all()[:100]
    context={
        'squirrels':squirrels
    }
    return render(request,'index.html', context)

def map(request):
    squirrels  = Squirrel.objects.all()[:100]
    context = {
       'squirrels' : squirrels,
       }
    return render(request, 'map.html', context) 

def sighting(request):
    return HttpResponse('Sightings') 

def sighting_update(request, unique_id): 
    Object = get_object_or_404(Squirrel, Unique_squirrel_id = unique_id) 
    form = Form(request.POST or None, instance = Object) 
    context = {'form':form} 
    if form.is_valid(): 
        Object = form.save(commit=False) 
        Object.save()
        return redirect('/sightings/')
    else: 
        context = {
            'form': form, 
        } 
        return render(request, 'sighting_id.html', context) 


def sighting_add(request): 
    if request.method == 'POST': 
        form = Form(request.POSE) 
        if form.is_valid():
            form.save()
        return redirect('/sighting/') 

    


