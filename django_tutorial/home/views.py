from django.shortcuts import render
from .form import CustomUserForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User
from .models import department,users,login,Leave_request
from . models import *
from.form import Leaveapplication
# Create your views here.
def index(request):
    person={
        'name':'Diya',
        'rollno':17,
        'class':'II BSC CS A ',
    }
    return render(request,'index.html',person)
def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You Can Login Now...!")
            return redirect('/login')
    return render(request,"register.html",{'form':form})
def login_page(request):
     return render(request,'login.html')
def user(request):
    dict_user={
        'users':users.objects.all()
    }
    return render(request,'user.html',dict_user)
def apply(request):
    if request.method=="POST":
        form=Leaveapplication(request.POST)
        if form.is_valid():
            form.save()
    form=Leaveapplication()
    dict_form={
        'form':form
    }
    return render(request,'apply.html',dict_form) 

def status(request):
     leave_requests = Leave_request.objects.all()
     return render(request, 'status.html', {'leave_requests': leave_requests})

def departmentname(request):
    dict_dept={
        'dept': department.objects.all()
    }
    return render(request,'department.html',dict_dept)
