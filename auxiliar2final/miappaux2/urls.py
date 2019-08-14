from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aeleccion', views.aeleccion, name='aeleccion'),
    path('equipodocente', views.equipodocente, name='equipodocente'),
]