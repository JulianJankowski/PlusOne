from django.contrib import admin
from django.urls import include
from django.urls import path
from PlusOneApp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('groups/', views.GroupListView.as_view(), name="groups"),
    path('groups/<str:pk>', views.GroupProfile.as_view(), name="group-profile"),
    path('activites/', views.ActivityListView.as_view(), name="activities"),
    path('activites/<str:pk>', views.ActivityDetail.as_view(), name="activity-detail"),
    path('account/', include('django.contrib.auth.urls')),
    path('user/<str:pk>', views.UserProfile.as_view(), name="account-profile"),
    path('register/', views.register, name="register"),
    path('create_group/', views.create_group, name="create_group"),
]