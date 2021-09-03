from django.shortcuts import render, HttpResponseRedirect, reverse
from app1.models import MyUser
from app1.forms import AddUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from bugtracker.settings import AUTH_USER_MODEL
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django import forms
from django.contrib import messages

# Create your views here.
def add_user(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            my_user1 = MyUser.objects.create_user(username=data['username'], password=data['password'])
            messages.success(request, 'User successfully created!', extra_tags='success')
            return HttpResponseRedirect(reverse('home'))
    form = AddUserForm()
    return render(request, 'generic_form.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            my_user = authenticate(request, username=data['username'], password=data['password'])
            if my_user:
                login(request, my_user)
                messages.success(request, 'User successfully logged in!', extra_tags='success')
                return HttpResponseRedirect(reverse('home'))

    form = LoginForm()
    return render(request, 'generic_form.html', {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, 'User successfully logged out!', extra_tags='success')
    return HttpResponseRedirect(request.GET.get('next', reverse('home')))