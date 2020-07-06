from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user   = models.OneToOneField(User,on_delete=models.CASCADE)
    profilePicture = models.ImageField(null=True)
    sex = models.CharField(default='None',max_length=10)
    bio = models.CharField(null=True,max_length=100)
    def __str__(self):
        return str(self.user)+' - '+self.bio
# class User(AbstractUser):
#     profile = models.OneToOneField(User,on_delete=models.CASCADE)

class Messages(models.Model): 
    message = models.TextField()
    timeSent = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,default=None)
    friend = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    def __str__(self):
        return str(self.user.user)+' - '+str(self.friend.friend) +' ==> '+self.message
class Friends(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default=None)
    friend = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    confirmed = models.BooleanField(default=False)
    Isent = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    def __str__(self):
        return self.friend.username 

class Groupp(models.Model):
    comment = models.TextField()
    timeSent = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return str(self.user.user.username)+ " : " + self.comment

class Forum(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    private = models.BooleanField(default=False)
    password = models.CharField(null=True ,max_length=50)
    group = models.ForeignKey(Groupp , on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user.user.username)+ " : " + self.name