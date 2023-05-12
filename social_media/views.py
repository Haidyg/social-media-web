from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UserForm, UpdateUserForm, UpdateProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Following, Post
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.hashers import make_password
import itertools
from .forms import RegisterForm


def home(request):
    print(f" Request {request}")
    user = request.user
    if request.user.is_authenticated:
        return render(request, 'home/index.html')
    else:
        return redirect('login')


def profile(request):
    return render(request, 'profile/index.html')

def login_request(request):
    context ={}
    print(f"request....................................")
    if request.method == 'POST':
        
        form = AuthenticationForm(request, data=request.POST)
        print(f'Form => {form}')    
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(f'email {password}')
        valid = form.is_valid()
        user = authenticate(request=request,username=username, password=password)
        print(f'Form {user}')
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('home')
        else:
            messages.error(request,"Invalid username or password.")
    form = UserForm()
    context['user_form'] = form
    print('Login')
    return render(request, 'login/index.html', context=context)

def register(request):
    context = {}
    print('inside register')
    if request.POST:
        form = RegisterForm(request.POST)
        valid = form.is_valid()
        
        print(f'inside Login2 {form}')
        if form.is_valid():
            print(f'form isValid {form}')
            form.save()
            print("form after save")
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            account = authenticate(username=username, password=raw_password)
            login(request)

            return redirect('home')
        else:
            form = RegisterForm()
            context['registration_form'] = form
            return render(request, 'register/index.html', context=context)
    form = RegisterForm()
    context['registration_form'] = form
    print('Registration')
    return render(request, 'register/index.html', context=context)


def friends(request):
    return render(request, 'friends/index.html')


def VerifyInput(username, password):
    error = []
    if len(username) > 4:
        error.append('Username should be at least 4 characters long')
    elif len(password) > 8:
        error.append('Password should be at least 8 characters long')
    else:
        print('OK')

    return error

# from django.views.generic import TemplateView

# class HomePageView(TemplateView):
#    template_name = "index.html"


# class AboutPageView(TemplateView):
#    template_name = "about.html"
# Create your views here.
