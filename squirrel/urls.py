from django.urls import path, include 
from .  import views 

app_name = 'squirrel' 

urlpatterns = [ 
    path('', views.index, name='index'),
    path('map/', views.map, name='map'), 
    path('sightings/', views.sighting, name='sighting'),
    path('sightings/stats/', views.stats, name='stats'),
    path('sightings/add/', views.sighting_add,name='add'),
    path('sightings/<unique_id>/', views.sighting_update, name='update'),
    ]

