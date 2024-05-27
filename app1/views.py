from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["Email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "your account has been successfully created.")
        return redirect("signin")

    return render(request, 'register.html')

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.username
            return render(request, "home.html", {"fname": fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect("signin")

    return render(request, 'login.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('signin') 

def movie(request):
    return render(request, 'movie.html')

def movies(request):
    return render(request, 'movies.html')

def TVshows(request):
    return render(request, 'TVshows.html')
