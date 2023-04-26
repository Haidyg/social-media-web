from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import UserForm,UpdateUserForm,UpdateProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import User,Following,Post
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.hashers import make_password
import itertools

def index(request):
    return HttpResponse("HELLOOOOO!")

def home(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'login/index.html')

def login2(request):
    return render(request, 'login2/index.html')

def register(request):
    return render(request, 'register/index.html')

def friends(request):
    return render(request, 'friends/index.html')

def VerifyInput(username,password):
    error=[] 
    if len(username) > 4:
        error.append('Username should be at least 4 characters long')
    elif len(password) > 8:
         error.append('Password should be at least 8 characters long')
    else:
        print('OK')
    
    return error

def RegisterUser(request):
    request.method='POST'
    username = request.POST['username']
    email = request.POST['email']
    password=request.POST['password']
    hashed_Password = make_password(password)











#from django.views.generic import TemplateView

#class HomePageView(TemplateView):
#    template_name = "index.html"


#class AboutPageView(TemplateView):
#    template_name = "about.html"
# Create your views here.
