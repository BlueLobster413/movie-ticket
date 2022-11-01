from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import formset_factory,modelformset_factory

# Create your views here.
def index(request):
    message = """
                Welcome to movie ticket booking system
            """
    return HttpResponse(message)

def index2(request):
    context = {}
    return render(request,"index.html",context)

def login(request):
    context = {}
    return render(request,"user_login.html",context)

def signup(request):
    context = {}
    return render(request,"user_signup.html",context)

def movie_detail(request):
    context = {}
    return render(request,"movie_detail.html",context)

def show_select(request):
    context = {}
    return render(request,"show_selection.html",context)

def seat_select(request):
    context = {}
    return render(request,"seat_selection.html",context)

def checkout(request):
    context = {}
    return render(request,"checkout.html",context)

def booked_ok(request):
    context = {}
    return render(request,"booking_ok.html",context)

