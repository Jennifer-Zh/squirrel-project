#from django.contrib import admin 
from django.urls import path, include 
from .  import views 

app_name = 'squirrel' 

urlpatterns = [ 
    path('', views.index),
    #path('map/', include('maps.urls')), 
    path('sighting/', views.sighting),
    #path('<int:Unique_squirrel_id>/', views.get_squirrel),
    #path('sighting/stats/', views.general_stats), 
]

