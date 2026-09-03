from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    profile_picture=models.ImageField(upload_to="profile_pictures/",blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User,blank=True,related_name="liked_posts")

    def __str__(self):
        return self.author.username