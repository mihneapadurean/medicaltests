from django import forms
from .models import Patient, Gender, User

class Login(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput)


def unique_mail(value):
    if User.objects.filter(email=value).count() != 0:
        raise forms.ValidationError("The email has to be unique")

class UserForm(forms.Form):
    GENDER_CHOICES = [g.name for g in Gender.objects.all()]

    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.EmailField(label="Email", max_length=100, validators=[unique_mail])
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", max_length=100, widget=forms.PasswordInput)
    city = forms.CharField(label="City", max_length=100)
    birth_day = forms.DateField(label="Date of Birth", widget=forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}))
    #gender = forms.ChoiceField(label="Gender", choices=GENDER_CHOICES, widget=forms.Select)

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise forms.ValidationError("The password and the confirmes password are not the same")


class RegisterPatient(UserForm):
    weight = forms.IntegerField(label="Weigth")

class RegisterMedic(UserForm):
    hospital = forms.CharField(label="Main Workplace", max_length=100)