from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Following, Profile,Post,Comment, UploadImage  

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
	username = forms.CharField(max_length=255)
	class Meta:
		model = User
		fields = ['username','email','password1', 'password2']


# Form for updating user email
class UpdateUserForm(forms.ModelForm):
	email = forms.EmailField(max_length=254, help_text='Required field')

	class Meta:
		model = User
		fields = ['email']


class AddFollower(forms.ModelForm):
	following_user = forms.IntegerField()
    

	class Meta:
		model = Following
		fields = ['following_user']
# Form for updating profile
class UpdateProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['status_info','profile_photo']



# Form for creating a post
class CreatePost(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = '__all__'  


# Form for creating a comment
class CreateComment(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ['comment_text']

class UserImage(forms.ModelForm):  
    class meta:  
        # To specify the model to be used to create form  
        models = UploadImage  
        # It includes all the fields of model  
        fields = '__all__'  