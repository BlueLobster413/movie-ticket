from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'), 
    path('login', views.login, name='login'), 
    path('movies', views.movies, name='movies'), 
    path('addfilm', views.add_movie, name='add movie'), 
    path('bookings', views.bookings, name='bookings'), 
    path('users', views.users, name='users'), 
]