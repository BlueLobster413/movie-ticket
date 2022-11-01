from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request,"dashboard.html",context)

def login(request):
    context = {}
    return render(request,"admin_login.html",context)

def movies(request):
    context = {}
    return render(request,"movies.html",context)

def bookings(request):
    context = {}
    return render(request,"bookings.html",context)

def users(request):
    context = {}
    return render(request,"users.html",context)