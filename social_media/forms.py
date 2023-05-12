from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile,Post,Comment



# Form for registering new user
class UserForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField(max_length=254, help_text='Required field')
	class Meta:
		model = User
		fields = ['email','password']

    
# Create your forms here.
class RegisterForm(UserCreationForm):
	password1 = forms.CharField(max_length=28)
	password2 = forms.CharField(max_length=28)
	email = forms.EmailField(max_length=254, help_text='Required field')
	class Meta:
		model = User
		fields = ['username','email','password1', 'password2']


# Form for updating user email
class UpdateUserForm(forms.ModelForm):
	email = forms.EmailField(max_length=254, help_text='Required field')

	class Meta:
		model = User
		fields = ['email']


# Form for updating profile
class UpdateProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['status_info','profile_photo']


# Form for creating a post
class CreatePost(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ['post_text','post_picture']


# Form for creating a comment
class CreateComment(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ['comment_text']