from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import TODO


def signup(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        email = request.POST["email"]
        pwd = request.POST["pwd"]
        my_user = User.objects.create_user(uname, email, pwd)
        my_user.save()
        return redirect('/login')
    return render(request, "signup.html")