from django.db import models
from django import forms

# Create your models here.
class admins(models.Model):
	# fields of the model
	firstname = models.CharField(max_length = 20) # a title field
	lastname = models.CharField(max_length = 20) # a title field
	email = models.EmailField(max_length=50) # a description field
	date_created = models.DateTimeField(auto_now_add = True) # a datetime field
	password = models.CharField(max_length=20, widget=forms.PasswordInput)
	# with their title name
	def __str__(self):
		return self.title

class films(models.Model):
    movie_name = models.CharField(max_length = 100)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField()
    show_times = models.CharField(max_length = 100)
    price = models.IntegerField()
    
    def __str__(self):
        return self.title

