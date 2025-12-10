from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    ROLES = [
        ['ADMIN','Admin'],
        ['USER','User'],
        ['MANAGER','Manager']
    ]

    roles = models.CharField(choices=ROLES,default='USER')

class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.name



class Task(models.Model):
    name= models.TextField(max_length=128)
    description = models.TextField(max_length=1285,blank=True,null=True)
    status = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    

