from django.urls import path, include
from django.contrib.auth import views as auth_views
from. import views
from .views import image_request 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.home, name='home'),
    path('login',views.login_request, name='login'),
    #path('account/login/',views.login_request, name='login'),
    path('profile',views.profile, name='profile'),
    path('register',views.register, name='register'),
    path('friends',views.friends, name='friends'),
    path('chat',views.chat, name='chat'),
    path('', image_request, name = "image-request")
]
