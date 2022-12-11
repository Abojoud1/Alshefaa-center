from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from . models import *
from .forms import *

# Create your views here.

def base(request):
    return render(request, 'base.html')

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('patientss')
        else:
            return redirect('login')
    else:
        return render(request,'authentication/login.html')

def logout_user(request):
    if request.method=='POST':
        logout(request)
        return redirect('login')
    return render(request,'authentication/logout.html')

def users(request):
    return render(request,'authentication/users.html',{'us':Authentication.objects.all()})

def adduser(request):
    if request.method =='POST':
        dataform=User_Forms(request.POST)
        if dataform.is_valid():
            dataform.save()
    return render(request,'authentication/adduser.html',{'us':User_Forms})


def removeuser(request,id):
    user_id=Authentication.objects.get(id=id)
    if request.method=='POST':
        user_id.delete()
        return redirect('userss')
    return render(request,'authentication/removeuser.html')

def updateuser(request,id):
    user_id=Authentication.objects.get(id=id)
    if request.method=='POST':
        user_save=User_Forms(request.POST,request.FILES,instance=user_id)
        if user_save.is_valid():
            user_save.save()
            return redirect('userss')
    else:
        user_save=User_Forms(instance=user_id)
    context={'form':user_save}
    return render(request,'authentication/updateuser.html',context)
