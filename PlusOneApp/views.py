import datetime

from django.shortcuts import render, get_object_or_404
from PlusOneApp.models import *
from PlusOneApp.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
def register(request):
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