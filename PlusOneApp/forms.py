import datetime

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from PlusOneApp.models import *
from django.db import models
from PlusOneApp.choices import *

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

class CreateEventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.fields['group'].queryset = self.user.account.group_set.all()

    name = forms.CharField()
    group = forms.ModelChoiceField(queryset=None, required=True)
    description = forms.CharField(widget=forms.Textarea)
    timeOccuring = forms.DateTimeField(label="Time Occuring", input_formats=['%d/%m/%Y %H:%M'])
    reccuring = forms.BooleanField()
    howOften = forms.ChoiceField(choices=RECCURING_CHOICES, label="How Often")

    activities = forms.ModelMultipleChoiceField(queryset=Activity.objects.all())

    class Meta:
        model = Event
        fields = ('name', 'group', 'description', 'timeOccuring', 'reccuring', 'howOften', 'activities')