from django.contrib import admin
from django.urls import path ,include
from project1 import views

urlpatterns = [
    path('',views.index,name="home"),
    path('shorti',views.shorti,name='shorti'),
    
]
