from django.shortcuts import render,redirect
from django.contrib.auth import (
	authenticate,
	# get_user_model,
	login,
	logout, )
# Create your views here.
from .forms import UserLoginForm ,UserRegisterForm

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password= password)
        login(request,user)
        return redirect("home")
    context = {
    "form":form,
    }
    return render(request, 'signin.html',context)

def register_view(request):
    title = "Register "
    form = UserRegisterForm (request.POST or None)
    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username , password= password)
        login(request,new_user)
        return redirect("home")
    context = {
    'form' : form,
    "title" : title,
    }
    return render(request,'signin.html',context)

def logout_view(request):
    logout(request)
    context = {
    "logout" : "You are sucessfully logged out ...."
    }
    return render(request,'index.html', context)
