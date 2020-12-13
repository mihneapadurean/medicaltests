from django.shortcuts import render
import django.contrib.auth as auth
from django.http import HttpResponse
from django.forms.utils import ErrorList
from django.shortcuts import redirect

from .forms import Login, RegisterPatient, RegisterMedic

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
        if form.is_valid:
            pass
    return render(request, 'register.html', {'category':category, 'form': form})

def check_user(request):
    return HttpResponse(request.user.username)