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
    squirrels  = Squirrel.objects.all()
    context = {
       'squirrels' : squirrels,
       }
    return render(request, 'sighting.html', context)


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
        form = Form(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('/sightings/')
    else:
        form = Form()
    return render(request, 'sighting_add.html', {'form':form})

def stats(request):
    total = Squirrel.objects.count()
    adultper=round(Squirrel.objects.filter(Age='Adult').count()/total,2)
    jueper=round(Squirrel.objects.filter(Age='Juvenile').count()/total,2)
    pmper=round(Squirrel.objects.filter(Shift='PM').count()/total,2)
    amper=round(Squirrel.objects.filter(Shift='AM').count()/total,2)
    
    running= Squirrel.objects.filter(Running=True).count()
    chasing=Squirrel.objects.filter(Chasing=True).count()
    climbing=Squirrel.objects.filter(Climbing=True).count()
    eating=Squirrel.objects.filter(Eating=True).count()
    tailflag=Squirrel.objects.filter(Tail_flags=True).count()
    tailtwitch=Squirrel.objects.filter(Tail_twitches=True).count()
    context = {
            'climbing':climbing,
            'running' : running,
            'chasing': chasing,
            'eating':eating,
            'tailflag':tailflag,
            'total':total,
            'adultper':adultper,
            'jueper':jueper,
            'pmper':pmper,
            'amper':amper,
            'tailtwitch':tailtwitch,
           }
    return render(request, 'stats.html', context)


