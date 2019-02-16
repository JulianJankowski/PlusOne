from django.shortcuts import render
from PlusOneApp.models import *

# Create your views here.

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