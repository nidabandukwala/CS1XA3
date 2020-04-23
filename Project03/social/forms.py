from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from social.models import UserInfo, Interest
class UpdateInfo(forms.Form):
           employment = forms.CharField(label="employment" ,max_length=30)
           location = forms.CharField(label ="location", max_length=50)
           birthday = forms.DateField(label="birthday")


