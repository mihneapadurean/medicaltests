from django.shortcuts import render
import django.contrib.auth as auth
from django.http import HttpResponse
from django.forms.utils import ErrorList
from django.shortcuts import redirect

from .forms import Login, RegisterPatient, RegisterMedic
from .models import User, Patient, Medic

# Create your views here.
def login(request):
    if request.method == 'GET':
        form = Login()
    elif request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid:
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('analysis:show_all')
            else:
                errors = form.add_error(None, "Login failed")
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect("login")

def register(request, category):
    category_to_form = {
        "patient": RegisterPatient,
        "medic": RegisterMedic
    }
    if request.method == "GET":
        form = category_to_form[category]()
    elif request.method == "POST":
        form = category_to_form[category](request.POST)
        if len(form.errors) == 0:
            auth.login(request, create_user(form).user)
            return redirect("analysis:show_all")
    return render(request, 'register.html', {'category':category, 'form': form})

def create_user(form):
    user_fields = ["first_name", "last_name", "email", "username", "password", "city", "birth_day", "gender"]
    additional_fields = list(set(["weight", "hospital"]) & set(form.cleaned_data))
    base_user = User(**{key: form.cleaned_data[key] for key in user_fields if key in form.cleaned_data.keys()})
    full_user = form.type_(user=base_user, **{key: form.cleaned_data[key] for key in additional_fields})
    base_user.save()
    full_user.save()
    return full_user

def check_user(request):
    return HttpResponse(request.user.username)