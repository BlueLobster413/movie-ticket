from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import  Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
# Create your views here.


def index(request):
    return render(request, 'account_index.html')

def staff_required(user):
    return user.is_authenticated and  user.is_staff

def is_user(user):
    return not user.is_staff

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(Group.objects.get(name='customer'))
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'account_create.html', {'form': form, 'msg': msg})


# def staff_login_view(request):
#     if request.user.is_authenticated:
#         if request.user.is_staff:
#             return redirect('/')
#     form = LoginForm(request.POST or None)
#     msg = None
#     if request.method == 'POST':
        
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None and user.is_staff:
#             # if user is not None and user.role==1:
#                 login(request, user)
#                 return redirect('/admin')
#             # elif user is not None and user.is_customer:
#             elif user is not None and not user.is_staff:
#             # elif user is not None and user.role==0:
#                 login(request, user)
#                 return redirect('/')
#             # elif user is not None and user.is_employee:
#             #     login(request, user)
#             #     return redirect('employee')
#             else:
#                 msg= 'invalid credentials'
#         else:
#             msg = 'error validating form'
#     return render(request, 'account_staff_login.html', {'form': form, 'msg': msg})

def login_view(request):
    if request.user.is_authenticated:
        # return render(request, 'account_index.html')
        return redirect('/')
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:
            # if user is not None and user.role==1:
                login(request, user)
                return redirect('/admin')
            # elif user is not None and user.is_customer:
            elif user is not None and not user.is_staff:
            # elif user is not None and user.role==0:
                login(request, user)
                return redirect('/')
            # elif user is not None and user.is_employee:
            #     login(request, user)
            #     return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'account_login.html', {'form': form, 'msg': msg})



@user_passes_test(staff_required, login_url='/adminlogin')
def admin(request):
    return render(request,'admin.html')

@login_required(login_url='/login')
def customer(request):
    return render(request,'customer.html')


def employee(request):
    return render(request,'employee.html')

def signout(request):
    logout(request)
    return redirect('/')
    # return HttpResponseRedirect("/")