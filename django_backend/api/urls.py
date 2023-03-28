from django.urls import path, include
from . import views
from django.shortcuts import render
from django.http import HttpResponse

urlpatterns =[
    path('index', views.index, name = 'index'), 
    path('return_jsondata', views.return_jsondata, name = 'return_jsondata'),

]