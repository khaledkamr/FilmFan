from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def movie(request):
    return render(request, 'movie.html')

def movies(request):
    return render(request, 'movies.html')

def register(request):
    return render(request, 'register.html')

def TVshows(request):
    return render(request, 'TVshows.html')
