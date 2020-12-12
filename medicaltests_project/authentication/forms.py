from django import forms
from .models import User

class Login(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput)