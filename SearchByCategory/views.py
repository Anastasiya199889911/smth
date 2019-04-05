from django.shortcuts import render
from . import models
from django.http import HttpResponse, JsonResponse
import json
import random
import requests
import bs4

# Create your views here.


def SearchByCategory(request):
    genres=models.Genre.objects.all()
    years=models.Year.objects.all()
    countries=models.Country.objects.all()
    ratings=models.Rating.objects.all()
    return render(request, 'SearchByCategory/../templates/Main/SearchByCategory.html', locals())


def SearchFilm(request):
    genre1 = request.GET.get("genre1")
    idGenre=(models.Genre.objects.filter(name=genre1))[0].id
    startYear = request.GET.get("startYear")
    endYear = request.GET.get("endYear")
    country = request.GET.get("country")
    idCountry=(models.Country.objects.filter(name=country))[0].id
    rating = request.GET.get("rating")
    films=models.Film.objects.all()

    if(genre1!='-Не выбрано-'):
        films=films.filter(filmbygenre__id_genre=idGenre)
    if(startYear!='-Не выбрано-'):
        films=films.filter(year__gte=startYear)
    if(endYear!='-Не выбрано-'):
        films=films.filter(year__lte=endYear)
    if(country!='-Не выбрано-'):
        films = films.filter(filmbycountry__id_country=idCountry)
    print('count ', films.count())
    if(rating!='0'):
        films=films.filter(rating=rating)

    film=[]
    number = random.randint(1, films.count() + 1)
    genres = models.FilmByGenre.objects.filter(id_film=films[number].id)
    genre = []
    for g in genres:
        genre.append(g.id_genre.name)
    countries = models.FilmByCountry.objects.filter(id_film=films[number].id)
    country = []
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

