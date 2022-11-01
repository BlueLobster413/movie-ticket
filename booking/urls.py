from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index2, name='index'), 
    path('login', views.login, name='user login'), 
    path('signup', views.signup, name='user signup'), 
    path('detail', views.movie_detail), 
    path('show', views.show_select), 
    path('seat', views.seat_select), 
    path('checkout', views.checkout), 
    path('booked', views.booked_ok), 
]