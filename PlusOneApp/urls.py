from django.contrib import admin
from django.urls import include
from django.urls import path
from PlusOneApp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('groups/', views.GroupListView.as_view(), name="groups"),
    path('book/<int:pk>', views.GroupProfile.as_view(), name="group-profile"),
    path('account/', include('django.contrib.auth.urls')),
    path('register/', views.register, name="register"),
]