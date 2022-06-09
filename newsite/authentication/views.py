from collections import UserList
from email import message
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core import serializers
from rest_framework import viewsets
from .serializers import self_serializer
from rest_framework.renderers import JSONRenderer


def listget(request):
    is_staff=request.GET['is_staff']
    user_list=User.objects.filter(is_staff=is_staff)
    return render(request,"authentication/display.html",{"user_list":user_list})

def listall2(request):
    user_list=User.objects.all()
    return render(request,"authentication/display.html",{"user_list":user_list})
    # return render(request, 'display.html', {'num':num})
    # user_list=User.objects.filter(id=user_id)

def getjsonall(request):
    user_list=User.objects.all()
    json_data=serializers.serialize('json',user_list)
    return HttpResponse(json_data, content_type='application/json')
    ## other ways
    # userjson=self_serializer(user_list,many=True)
    # json_data=JSONRenderer().render(userjson.data)
    # fields=('userjson.username','userjson.email')

def getjson(request,id):
    user_list=User.objects.get(id=id)
    userjson=self_serializer(user_list)
    json_data=JSONRenderer().render(userjson.data)
    return HttpResponse(json_data, content_type='application/json')
    # userjson=serializers.serialize('json',user_list)

def listall(request,user_id):
    user_list=User.objects.filter(id=user_id)
    return render(request,"authentication/display.html",{"user_list":user_list})
    # user_list=User.objects.all()
    # return render(request, 'display.html', {'num':num})

def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect("home")
    return render(request,"authentication/signup.html")

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass1']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            firstname=user.first_name
            return render(request,'authentication/index.html',{'firstname': firstname})
        else:
            messages.error(request,"Bad Connection")
            return redirect('home')
    return render(request,"authentication/signin.html")

def signout(request, id : str = ""):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('home')