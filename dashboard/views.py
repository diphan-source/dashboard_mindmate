from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


from dashboard.utils import sidebar_menu

# Create your views here.

def home(request):
    return render(request, 'index.html', { 'links': sidebar_menu})


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    return HttpResponseRedirect('/dashboard')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('login[password]')
        print(f"username: {username}, password: {password}")
        user = authenticate(email=username, password=password)
        print(f"User: {user}")
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


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')