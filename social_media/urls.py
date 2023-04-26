from django.urls import path, include
from django.contrib.auth import views as auth_views
from. import views


urlpatterns = [
    path('',views.index, name='index'),
    path('login',views.login, name='login'),
    path('login2',views.login2, name='login2'),
    path('register',views.register, name='register'),
    path('friends',views.friends, name='friends'),
    path('home',views.home, name='home'),

]