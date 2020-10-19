#from django.contrib import admin 
from django.urls import path, include 
from .  import views 

app_name = 'squirrel' 

urlpatterns = [ 
    path('', views.index),
    path('map/', views.map, name='map'), 
    path('sightings/', views.sighting),
    path('sightings/add', views.sighting_add,name='add'),
    path('sightings/<unique_id>/', views.sighting_update, name='update'),
    #path('sighting/stats/', views.general_stats), 
]

