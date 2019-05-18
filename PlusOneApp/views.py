import datetime

from django.shortcuts import render, get_object_or_404
from PlusOneApp.models import *
from PlusOneApp.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import generic

# Create your views here.
def register(request):
    if(request.user.is_authenticated):
        return redirect("index")
    if(request.method == "POST"):
        form = RegistrationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            user.refresh_from_db()
            user.account.DOB = form.cleaned_data.get('DOB')
            user.account.profilePic = form.cleaned_data.get('profilePic')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('index')
    
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def create_group(request):
    if(request.user.is_authenticated == False):
        return redirect("index")
    if(request.method == "POST"):
        form = CreateGroupForm(request.POST)
        if(form.is_valid()):
            group = form.save()
            group.refresh_from_db()
            group.title = form.cleaned_data.get('title')
            group.members.set(form.cleaned_data.get('members'))
            group.description = form.cleaned_data.get('description')
            group.idealNum = form.cleaned_data.get('idealNum')
            group.activities.set(form.cleaned_data.get('activities'))
            group.profilePic = form.cleaned_data.get('profilePic')
            group.save()
            return redirect('/groups/' + group.title)
    else:
        form = CreateGroupForm()
    return render(request, 'create_group.html', {'form' : form})

def create_event(request):
    if(request.user.is_authenticated == False):
        return redirect("index")
    if(request.method == "POST"):
        form = CreateEventForm(request.POST, user=request.user)
    
    else:
        form = CreateEventForm(user=request.user)
    return render(request, 'create_event.html', {'form' : form})

class GroupListView(generic.ListView):
    model = Group
    context_object_name = 'group_list'
    queryset = Group.objects.all()
    template_name = 'groups/mylist.html'

class GroupProfile(generic.DetailView):
    model = Group

class ActivityListView(generic.ListView):
    model = Activity
    context_object_name = 'activity_list'
    queryset = Activity.objects.all()
    template_name = 'activities/mylist.html'

class ActivityDetail(generic.DetailView):
    model = Activity

class UserProfile(generic.DetailView):
    model = Account

def index(request):
    numGroups = Group.objects.all().count()
    numAccounts = Account.objects.all().count()
    numActivities = Activity.objects.all().count()

    context = {
        'Groups' : numGroups,
        'Accounts' : numAccounts,
        'Activities' : numActivities,
    }

    return render(request, 'index.html', context = context)