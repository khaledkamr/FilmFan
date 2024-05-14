from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.username
            return render(request, "authentication/home.html", {"fname": fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect("home")

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["Email"]
        pass1 = (request.POST["pass1"])
        pass2 = request.POST["pass2"]

    # if User.objects.filter(username=username):
    #     messages.error(request, "User name already exist! please try other user name")
    #     return redirect("register")
    
    # if User.objects.filter(email=email):
    #     messages.error(request, "Email already registered!")
    #     return redirect("register")
    
    # if len(username) > 15:
    #     messages.error(request, "Username must be under 15 characters")
    
    # if pass1 != pass2:
    #     messages.error(request, "passwords didn't match!")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "your account has been successfully created.")
        return redirect("home")

    return render(request, 'register.html')

def movie(request):
    return render(request, 'movie.html')

def movies(request):
    return render(request, 'movies.html')

def TVshows(request):
    return render(request, 'TVshows.html')
