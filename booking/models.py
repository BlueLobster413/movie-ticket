# from this import d
from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from traitlets import default

# class Users(AbstractUser):
#     is_theatre_staff = models.BooleanField('staff status', default=False)


# Create your models here.
# class users(models.Model):
#     firstname = models.CharField(max_length = 20,default="")
#     lastname = models.CharField(max_length = 20,default="")
#     email = models.EmailField(max_length=50)
#     age = models.IntegerField(default=0)
#     date_created = models.DateTimeField(auto_now_add = True)
#     password = models.CharField(max_length=20, default="")
#     def __str__(self):
#         return self.title
