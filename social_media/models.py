from django.db import models
from django.contrib.auth.models import User


# Model for user profile
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	id = models.AutoField(primary_key=True)
	profile_photo = models.FileField(default='default.jpg', upload_to='profile_photos', null=True)
	status_info = models.CharField(default="Enter status", max_length=1000) 
	birth_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return f'{self.user.username} Profile'
	

# Model for storing post
class Post(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	id = models.AutoField(primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True)
	post_text = models.CharField(max_length=2000)
	post_picture = models.FileField(default="default.jpg",upload_to='post_picture')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	

	def __str__(self):
		return self.user.username


# Model for storing poeple who follow
class Following(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
	id = models.AutoField(primary_key=True)
	following_user = models.IntegerField(null=False, blank=False, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


# Model for storing comment
class Comment(models.Model):
	post = models.ForeignKey(Post,on_delete = models.CASCADE)
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	comment_text = models.CharField(default="",max_length=2000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
	post = models.ForeignKey(Post,on_delete = models.CASCADE)
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)