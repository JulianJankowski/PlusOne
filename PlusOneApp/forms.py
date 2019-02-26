import datetime

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.CharField()
    DOB = forms.DateField()
    profilePic = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email', 'password1', 'password2', 'DOB', 'profilePic')