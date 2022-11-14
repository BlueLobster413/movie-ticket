from django.shortcuts import render, HttpResponseRedirect
from .forms import filmForm
from .models import film
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
from django.template.context_processors import csrf
# Create your views here.
from accounts.views import staff_required, is_user

# @login_required(login_url='/accounts/adminlogin')
@user_passes_test(staff_required, login_url='/accounts/adminlogin')
def index(request):
    context = {}
    return render(request,"dashboard.html",context)

def login(request):
    context = {}
    return render(request,"admin_login.html",context)

def movies(request):
    context = {}
    movies = film.objects.filter(deleted=False).values_list('id','movie_name','date_added', named=True)
    context = {
    'films': movies
    }
    return render(request,"movies.html",context)

def add_movie(request):
    context = {}
    context.update(csrf(request))

    if(request.method == "POST"):
        fn=request.POST['fn']
        fl=request.POST['fl']
        fy=request.POST['fy']
        fsd=request.POST['fsd']
        fed=request.POST['fed']
        fst1=request.POST['fst1']
        fst2=request.POST['fst2']
        fst3=request.POST['fst3']
        fp=request.POST['fp']
        fu=request.POST['fu']
        fa=request.POST.get('fa', False);
        contact=film.objects.create(movie_name=fn,movie_lang=fl,movie_year=fy,start_date=fsd,end_date=fed,showtime1=fst1,
        showtime2=fst2,showtime3=fst3,price=fp,url=fu,active=fa)
        # messages.success(request, "Film sdded successfully")
        context = {'message':"Success"}
        
    # context['form']= form
    return render(request,"create_movie.html",context)

def edit_movie(request, id):
    context = {}
    context["film"] = film.objects.get(id = id)  
    
    if(request.method == "POST"):
        fn=request.POST['fn']
        fl=request.POST['fl']
        fy=request.POST['fy']
        fsd=request.POST['fsd']
        fed=request.POST['fed']
        fst1=request.POST['fst1']
        fst2=request.POST['fst2']
        fst3=request.POST['fst3']
        fp=request.POST['fp']
        fu=request.POST['fu']
        fa=request.POST.get('fa', False);
        film.objects.filter(id=id).update(movie_name=fn,movie_lang=fl,movie_year=fy,start_date=fsd,end_date=fed,showtime1=fst1,
        showtime2=fst2,showtime3=fst3,price=fp,url=fu,active=fa)
        return HttpResponseRedirect("/detail/"+str(id))

    return render(request, "edit_movie.html", context)

def delete_movie(request, id):
    film.objects.filter(id=id).update(deleted=True)
    return HttpResponseRedirect("/admin/movies")
    


def bookings(request):
    context = {}
    return render(request,"bookings.html",context)

def users(request):
    context = {}
    return render(request,"users.html",context)