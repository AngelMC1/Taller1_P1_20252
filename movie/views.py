from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def home (request):
    #return HttpResponse('<h1> Welcome to Home Page </h1>')
    #return render(request, 'home.html')
    #return render (request, 'home.html', {'name':'Miguel Angel Correa'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        # lista únicamente la(s) película(s) cuyo título contiene el nombre buscado
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else: 
        # lista todas las películas de la base de datos
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies': movies})
   

def About (request):
    return render (request, 'about.html')
# Create your views here.
