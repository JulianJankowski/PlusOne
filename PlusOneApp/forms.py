import datetime

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from PlusOneApp.models import *

class RegistrationForm(UserCreationForm):
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.CharField()
    DOB = forms.DateField()
    profilePic = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email', 'password1', 'password2', 'DOB', 'profilePic')

class CreateGroupForm(forms.ModelForm):
    title = forms.CharField()
    members = forms.ModelMultipleChoiceField(queryset=Account.objects.all(), required=False)
    description = forms.CharField()
    idealNum = forms.IntegerField()
    activities = forms.ModelMultipleChoiceField(queryset=Activity.objects.all(), required=False)
    profilePic = forms.ImageField(required=False)

    class Meta:
        model = Group
        fields = ('title', 'members', 'description', 'idealNum', 'activities', 'profilePic')