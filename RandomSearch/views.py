from django.shortcuts import render
import requests
import bs4
from . import models
import random
from django.http import HttpResponse, JsonResponse
import json
import lxml.html

# Create your views here.


def RandomSearch(request):
    return render(request, 'RandomSearch/../templates/Main/RandomSearch.html', locals())


def SearchFilm(request):
    film=[]
    films=models.Film.objects.all()
    number=random.randint(1,films.count()+1)
    genres=models.FilmByGenre.objects.filter(id_film=films[number].id)
    genre=[]
    for g in genres:
        genre.append(g.id_genre.name)
    countries=models.FilmByCountry.objects.filter(id_film=films[number].id)
    country=[]
    for c in countries:
        country.append(c.id_country.name)
    film.append(films[number].name)
    film.append(films[number].image)
    film.append(films[number].original_name)
    film.append(genre)
    film.append(films[number].year)
    film.append(country)
    film.append(films[number].duration)
    film.append(films[number].producer)
    film.append(films[number].rating)
    film.append(films[number].text)
    film.append(123)
    return HttpResponse(json.dumps({'data': film}))