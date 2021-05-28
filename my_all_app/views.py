from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.conf import settings
from .forms import IndexForm


def view_login(request):
    """view for login"""
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'my_all_app/index.html')
        return render(request, 'my_all_app/login.html')
    return render(request, 'my_all_app/login.html')


def index(request):
    if request.user.is_authenticated:
        return render(request, 'my_all_app/index.html')
    else:
        return render(request, 'my_all_app/login.html')


def add(request):
    if request.user.is_authenticated:
        return render(request, 'my_all_app/add.html')
    else:
        return render(request, 'my_all_app/login.html')


def manage(request):
    if request.user.is_authenticated:
        return render(request, 'my_all_app/manage.html')
    else:
        return render(request, 'my_all_app/login.html')


def history(request):
    if request.user.is_authenticated:
        return render(request, 'my_all_app/history.html')
    else:
        return render(request, 'my_all_app/login.html')


def calculator(request):
    if request.user.is_authenticated:
        return render(request, 'my_all_app/calculator.html')
    else:
        return render(request, 'my_all_app/login.html')


def setting(request):
    if request.user.is_authenticated:
        form = IndexForm()
        return render(request, 'my_all_app/setting.html',{'form': form})
    else:
        return render(request, 'my_all_app/login.html')

