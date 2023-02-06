from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from dashboard.utils import sidebar_menu

# Create your views here.

# create is_logged_in decorator
def is_logged_in(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def home(request):
    return render(request, 'index.html', { 'links': sidebar_menu})


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    return HttpResponseRedirect('/dashboard')


@is_logged_in
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('login[password]')
        user = authenticate(email=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard')
            else:
                return render(request, 'login.html', {'error': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error': 'Invalid login details'})
    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')