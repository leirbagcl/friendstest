from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 255, default = 'name')
    username = models.CharField(max_length = 255, default = 'username')
    password= models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Friends(models.Model):
    friend_name = models.CharField(max_length = 255, default = 'friend_name')
    friends = models.ManyToManyField(User, related_name = "friends")
    connection = models.ForeignKey(User,related_name = 'connection_user', on_delete = models.CASCADE, null = True)
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at=models.DateTimeField(auto_now = True)