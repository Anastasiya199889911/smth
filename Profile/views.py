from django.shortcuts import render
import requests
import bs4
from . import models
import random
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
import lxml.html
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def Profile(request):
    id=request.session.get('userid','no')
    if(id!='no'):
        id = request.session['userid']
        name = request.session['username']
        # email = request.session['useremail']
        return render(request, 'Profile/Profile.html', locals())
    else:
        return render(request, 'Main/Authorization.html', locals())


def RandomSearch(request):
    id = request.session['userid']
    name = request.session['username']
    return render(request, 'Profile/RandomSearch.html', locals())

def Profile_Random_SearchFilm(request):
    print(1111111111)
    film=[]
    print(film)
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
    print(film)
    return HttpResponse(json.dumps({'data': film}))


def SearchByCategory(request):
    id = request.session['userid']
    name = request.session['username']
    genres=models.Genre.objects.all()
    years=models.Year.objects.all()
    countries=models.Country.objects.all()
    ratings=models.Rating.objects.all()
    return render(request, 'Profile/SearchByCategory.html', locals())


def Profile_Category_SearchFilm(request):
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


def Exit(request):
    logout(request)
    return HttpResponseRedirect("/")