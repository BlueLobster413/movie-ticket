from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request,"admin_dashboard.html",context)
def login(request):
    context = {}
    return render(request,"admin_login.html",context)