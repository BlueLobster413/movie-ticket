from django.db import models
# from django.forms import *

# Create your models here.
# class admins(models.Model):
# 	# fields of the model
# 	firstname = models.CharField(max_length = 20) # a title field
# 	lastname = models.CharField(max_length = 20) # a title field
# 	email = models.EmailField(max_length=50) # a description field
# 	date_created = models.DateTimeField(auto_now_add = True) # a datetime field
#	password = models.CharField(max_length=20, widget=forms.PasswordInput)
# 	# with their title name
# 	def __str__(self):
# 		return self.title

class film(models.Model):

    movie_name = models.CharField(max_length = 100)
    movie_lang = models.CharField(blank=True, null=True,max_length = 100)
    movie_year = models.IntegerField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    showtime1 = models.TimeField(auto_now=False, auto_now_add=False)
    showtime2 = models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    showtime3 = models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    price = models.IntegerField()
    url = models.URLField(blank=True, null=True)
    active = models.BooleanField()
    date_added = models.DateField(auto_now=False, auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.movie_name

