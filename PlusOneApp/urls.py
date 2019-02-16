from django.contrib import admin
from django.urls import include
from django.urls import path
from PlusOneApp import views

urlpatterns = [
    path('', views.index, name="index")
]