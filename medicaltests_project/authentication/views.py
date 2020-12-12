from django.shortcuts import render
import django.contrib.auth as auth
from django.http import HttpResponse
from django.forms.utils import ErrorList
from django.shortcuts import redirect

from .forms import Login

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
                return redirect('check_user')
            else:
                errors = form.add_error(None, "Login failed")
    return render(request, 'login.html', {'form': form})

def check_user(request):
    return HttpResponse(request.user.username)