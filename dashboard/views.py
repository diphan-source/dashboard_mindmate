from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from dashboard.utils import sidebar_menu
from dashboard.models import User

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

@login_required
def add_admin_user(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        first_name = request.POST.get('first_name').strip()
        last_name = request.POST.get('last_name').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()

        if not username or not first_name or not last_name or not email or not password:
            return render(request, 'add_admin_user.html', {'error': 'All fields are required', 'links': sidebar_menu})
        
        existing = User.objects.filter(email=email).first()
        if existing:
            return render(request, 'add_admin_user.html', {'error': 'Email already exists', 'links': sidebar_menu})

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.is_staff = True
        user.save()
        return HttpResponseRedirect('/admin_users')

    return render(request, 'add_admin_user.html', {'links': sidebar_menu})


@login_required
def admin_users(request):
    users = User.objects.filter(is_staff=True)
    return render(request, 'admin_users.html', {'users': users, 'links': sidebar_menu})



@login_required
def delete_admin_user(request, user_id):
    user = User.objects.filter(id=user_id).first()
    # delete user if exists and not superuser
    if user and not user.is_superuser:
        user.delete()
    return HttpResponseRedirect('/admin_users')

@login_required
def edit_admin_user(request, user_id):
    user = User.objects.filter(id=user_id).first()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        existing = User.objects.filter(email=email).first()
        if existing and existing.id != user.id:
            return render(request, 'edit_admin_user.html', {'error': 'Email already exists', 'links': sidebar_menu, 'user': user})

        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return HttpResponseRedirect('/admin_users')

    return render(request, 'edit_admin_user.html', {'links': sidebar_menu, 'user': user})


