from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .forms import AddFollower, UserForm, UpdateUserForm, UpdateProfileForm
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
from django.contrib import messages
from .forms import UserImage
from .models import UploadImage  
from .forms import UserImage, CreatePost


@login_required
def home(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)

        if form.is_valid():
            post_text = form.cleaned_data.get('post_text')
            form.save() 
            
        return HttpResponseRedirect("/home")
    
    else:
        form = CreatePost()  
        user = request.user
        followers = Following.objects.filter(user=request.user) #btnady mn el models Following , el user eli 3amaal login 
        posts = Post.objects.filter(user=request.user)
        user_followers: list = [] #array w mshena ala kol wahd mn eli gbnahom fo2  mn el followers
        for user in followers:
            user_follower = User.objects.filter(id=user.following_user).first()
            user_followers.append(user_follower)
        
        return render(request, 'home/index.html', {"followers": user_followers,
                                                   'form':form , 'posts':posts}) #bb3at ll front end 


@login_required
def chat(request):
    
    user = request.user
    followers = Following.objects.filter(user=request.user)
    user_followers: list = []
    for user in followers:
        user_follower = User.objects.filter(id=user.following_user).first() #awl row fl results bt3t el filter , byrg3 row wahd bas msh array 
        user_followers.append(user_follower)
    
    return render(request, 'chat/index.html', {"followers": user_followers})

def image_request(request):  
    if request.method == 'POST':  
        form = UserImage(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            img_object = form.instance  # el instance bt3 el sora nfsaha 
            return render(request, 'home.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImage()  
    return render(request, 'home.html', {'form': form})  


def login_request(request):
    context ={} #dictionary 
    form = AuthenticationForm(request, data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            valid = form.is_valid()
            user = authenticate(request=request,username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
        else:
            messages.error(request,"Invalid username or password.")
    form = UserForm()
    context['user_form'] = form #tari2a tanya ll user form 
    return render(request, 'login/index.html', context=context)


def register(request):
    context = {} #benhot feha el data el hanmlaha fel frontend
    if request.POST: # insert 
        form = RegisterForm(request.POST) #user 3amlaha submit
        valid = form.is_valid()
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            account = authenticate(username=username, password=raw_password) #enhom mawgodeen fel backend w law mawgodeen hatrg3 el user obj 
            user = User.objects.get(username=username) # hatrga3 none 
            login(request,user) #function gahza f django esmha loginn btakhod args  w bet3ml login 3al page w tehot cookies fel browser 3shan akon loged in
            return redirect('home')
        else:
            context['registration_form'] = form
            return render(request, 'register/index.html', {'form': form}) 

    form = RegisterForm()
    context['registration_form'] = form
    return render(request, 'register/index.html', context=context)

@login_required
def friends(request):
    followers = Following.objects.filter(user=request.user)
    user_followers: list = [] #array w ashan lma add friend yhotaha fl list 
    
    for user in followers:
        user_follower = User.objects.filter(id=user.following_user).first() #filter betrga3 array ama el first obj
        user_followers.append(user_follower) # w byhot hena 
    
    return render(request, 'friends/index.html', {"followers": user_followers})

@login_required
def profile(request):
    user_followers: list = []
    db_followers: list =[]
    if request.method == 'POST' and request.POST.get('following_user') :
        following= Following()
        following.user = request.user
        following.following_user = request.POST.get('following_user') 
        following.save()

    #betrga3 hagat ktera bas lama ba3mel first betrga3 haga wahda bas
    db_friends = User.objects.filter().exclude(username=request.user.username) #aknaha where fel db w betrga3 hagat kter bas law oltlo id=id
    followers = Following.objects.filter(user=request.user)
    user_followers: list = [] #array w ashan lma add friend yhotaha fl list 
    
    for user in followers: #hayrg3o bel id bas lama 3amlnaha el for loop 3shan negeb el data bet3ahom
        user_follower = User.objects.filter(id=user.following_user).first()
        user_followers.append(user_follower)

    for friend in db_friends: #benshel el nas el homa  
        if friend not in user_followers:
          db_followers.append(friend)
    return render(request, 'profile/index.html' ,  {"db_friends": db_followers })

