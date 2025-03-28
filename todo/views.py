from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import TODO
from django.http import HttpResponse


def signup(request):
    logged_in_user = request.user
    if logged_in_user.is_authenticated:
        return redirect('/todo')
    if request.method == "POST":
        uname = request.POST["uname"]
        email = request.POST["email"]
        pwd = request.POST["pwd"]
        my_user = User.objects.create_user(uname, email, pwd)
        my_user.save()
        return redirect('/login')
    return render(request, "signup.html")

def loginn(request):
    logged_in_user = request.user
    if logged_in_user.is_authenticated:
        return redirect('/todo')
    if request.method == "POST":
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        print(uname, pwd)
        
        user = authenticate(request, username = uname, password = pwd)
        if user is not None:
            login(request, user)
            return redirect('/todo')
        else:
            return redirect('/login')
    return render(request, "login.html")

def todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        print(title)
        obj = TODO(title=title, user = request.user)
        obj.save()
        return redirect('/todo')
    items = TODO.objects.filter(user= request.user).order_by("-date")
    return render(request, 'todo.html', {'items': items})