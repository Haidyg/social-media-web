from django.urls import path, include
from django.contrib.auth import views as auth_views
from. import views

urlpatterns = [
    path('home',views.home, name='home'),
    path('login',views.login_request, name='login'),
    path('profile',views.profile, name='profile'),
    path('register',views.register, name='register'),
    path('friends',views.friends, name='friends'),
]
