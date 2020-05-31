from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user   = models.OneToOneField(User,on_delete=models.CASCADE)
    profilePicture = models.ImageField(null=True)
    sex = models.CharField(default='None',max_length=10)
    bio = models.CharField(null=True,max_length=100)
    def __str__(self):
        return self.user.username 
# class User(AbstractUser):
#     profile = models.OneToOneField(User,on_delete=models.CASCADE)

class Messages(models.Model):
    message = models.TextField()
    timeSent = models.DateTimeField(auto_now=True)
    whos = models.BooleanField(default = True)
class Friends(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default=None)
    friend = models.ForeignKey(User,on_delete=models.CASCADE,default=None,unique=True)
    messages= models.OneToOneField(Messages, on_delete=models.CASCADE ,null=True)
    confirmed = models.BooleanField(default=False)
    def __str__(self):
        return self.friend.username 