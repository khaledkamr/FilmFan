from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('movie', views.movie, name='movie'),
    path('movies', views.movies, name='movies'),
    path('register', views.register, name='register'),
    path('TVshows', views.TVshows, name='TVshows'),
]