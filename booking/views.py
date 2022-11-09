from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import formset_factory,modelformset_factory
from webadmin.models import film

# Create your views here.
def index(request):
    message = """
                Welcome to movie ticket booking system
            """
    return HttpResponse(message)

def home(request):
    context = {}
    movies = film.objects.filter(deleted=False).values_list('id','movie_name','url', named=True)
    context = {
    'films': movies
    }
    return render(request,"index.html", context)

def login(request):
    if (request.method == "POST"):
        email = request.POST.get('email')
        passw = request.POST.get('pass')

    return render(request,"user_login.html")

def signup(request):

    if (request.method == "POST"):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')
        email = request.POST.get('fname')
        passw = request.POST.get('pass')

    return render(request,"user_signup.html")

def movie_detail(request,id):
    context = {}
    context["film"] = film.objects.get(id = id)  
    return render(request,"movie_detail.html",context)

def show_select(request):
    context = {}
    if(request.method == "GET" and len(request.GET)!=0):
        # print("get raised")
        date = request.GET['date']
        films = film.objects.filter(end_date__gte=date).values_list('id','movie_name','url','showtime1','showtime2','showtime3', named=True)
        context = {'films':films,'date':date}
    
    return render(request,"show_selection.html",context)

def seat_select(request):
    context = {} 
    if(request.method == "GET" and len(request.GET)==3):
        id = request.GET['mid']
        st = request.GET['st']
        d = request.GET['d']
        context["film"] = film.objects.get(id = id)
        context['date'] = d
        context['st'] = st
    return render(request,"seat_selection.html",context)

def checkout(request):
    context = {}
    return render(request,"checkout.html",context)

def booked_ok(request):
    context = {}
    return render(request,"booking_ok.html",context)

