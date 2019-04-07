from django.shortcuts import render,reverse,redirect
import requests
import bs4
from . import models
import random
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from datetime import datetime, timedelta
import lxml.html
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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
    album=models.Album.objects.filter(id_user=id)
    return render(request, 'Profile/RandomSearch.html', locals())

def Profile_Random_SearchFilm(request):
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
    likes=models.FilmLike.objects.filter(id_film=films[number].id)
    id = request.session['userid']
    user=models.AuthUser.objects.filter(id=id)
    likeFlag=False
    if(len(models.FilmLike.objects.filter(id_film=films[number].id, id_user=id))!=0):
        likeFlag=True
    clockFlag = False
    if (len(models.FilmWantSee.objects.filter(id_film=films[number].id, id_user=id)) != 0):
        clockFlag = True
    starFlag = False
    if (len(models.FilmFavorite.objects.filter(id_film=films[number].id, id_user=id)) != 0):
        starFlag = True

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
    film.append(len(likes))
    film.append(likeFlag)
    comments=models.FilmComment.objects.filter(id_film=films[number].id).order_by('-date_time')
    comment=[]
    for c in comments:
        com=[]
        com.append(c.id_user.first_name)
        com.append(c.date_time.strftime("%d-%m-%Y %H:%M"))
        com.append(c.text)
        comment.append(com)
    film.append(comment)
    film.append(clockFlag)
    film.append(starFlag)
    print(comment)
    last=models.FilmLast.objects.order_by('date').filter(id_user=id)
    if(len(last)>=12):
        last[0].id_film=films[number]
        last[0].date=datetime.now()+timedelta(hours=3)
        last[0].save()
    else:
        last=models.FilmLast(id_user=user[0],id_film=films[number],date=(datetime.now()+timedelta(hours=3)))
        last.save()
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
    likes = models.FilmLike.objects.filter(id_film=films[number].id)
    id = request.session['userid']
    user = models.AuthUser.objects.filter(id=id)
    likeFlag = False
    if (len(models.FilmLike.objects.filter(id_film=films[number].id, id_user=id)) != 0):
        likeFlag = True
    clockFlag = False
    if (len(models.FilmWantSee.objects.filter(id_film=films[number].id, id_user=id)) != 0):
        clockFlag = True
    starFlag = False
    if (len(models.FilmFavorite.objects.filter(id_film=films[number].id, id_user=id)) != 0):
        starFlag = True

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
    film.append(len(likes))
    film.append(likeFlag)
    comments = models.FilmComment.objects.filter(id_film=films[number].id).order_by('-date_time')
    comment = []
    for c in comments:
        com = []
        com.append(c.id_user.first_name)
        com.append(c.date_time.strftime("%d-%m-%Y %H:%M"))
        com.append(c.text)
        comment.append(com)
    film.append(comment)
    film.append(clockFlag)
    film.append(starFlag)
    print(comment)
    last = models.FilmLast.objects.order_by('date').filter(id_user=id)
    if (len(last) >= 12):
        last[0].id_film = films[number]
        last[0].date = datetime.now() + timedelta(hours=3)
        last[0].save()
    else:
        last = models.FilmLast(id_user=user[0], id_film=films[number], date=(datetime.now() + timedelta(hours=3)))
        last.save()
    return HttpResponse(json.dumps({'data': film}))

def AddLike(request):
    filmName = request.GET.get("filmName")
    filmName=filmName.strip()
    filmId=models.Film.objects.filter(name=filmName)
    print(filmId[0])
    id = request.session['userid']
    user=models.AuthUser.objects.filter(id=id)
    likeFlag = False
    if(len(models.FilmLike.objects.filter(id_film_id=filmId[0].id, id_user_id=id))==0):
        print(0000000)
        filmLike=models.FilmLike(id_user=user[0], id_film=filmId[0])
        filmLike.save()
        likeFlag = True
    else:
        print(1111111)
        filmLike=models.FilmLike.objects.get(id_user=user[0], id_film=filmId[0])
        filmLike.delete()
        likeFlag=False

    likes = models.FilmLike.objects.filter(id_film=filmId[0].id)

    # if (len(models.FilmLike.objects.filter(id_film_id=filmId[0].id, id_user_id=id)) != 0):


    film=[]
    film.append(len(likes))
    film.append(likeFlag)
    return HttpResponse(json.dumps({'data': film}))


def Liked(request):
    id=request.session['userid']
    name = request.session['username']
    # films=models.FilmLike.objects.filter(id_film_id=filmId[0].id, id_user_id=id)
    films=models.Film.objects.filter(filmlike__id_user=id).order_by('id')
    return render(request, 'Profile/Liked.html', locals())


def AddComment(request):
    filmName = request.GET.get("filmName")
    commentText = request.GET.get("commentText")
    filmName=filmName.strip()
    print(filmName)
    filmId=models.Film.objects.filter(name=filmName)
    print(filmId[0])

    id = request.session['userid']
    user=models.AuthUser.objects.filter(id=id)
    print(user[0])
    now = datetime.now()+timedelta(hours=3)
    filmComment=models.FilmComment(id_user=user[0], id_film=filmId[0],date_time=now, text=commentText)
    filmComment.save()

    comments = models.FilmComment.objects.filter(id_film=filmId[0].id).order_by('-date_time')

    # if (len(models.FilmLike.objects.filter(id_film_id=filmId[0].id, id_user_id=id)) != 0):
    comment = []
    for c in comments:
        com = []
        com.append(c.id_user.first_name)
        com.append(c.date_time.strftime("%d-%m-%Y %H:%M"))
        com.append(c.text)
        comment.append(com)
    print(comment)
    return HttpResponse(json.dumps({'data': comment}))

def AddWantSee(request):
    filmName = request.GET.get("filmName")
    filmName = filmName.strip()
    filmId=models.Film.objects.filter(name=filmName)
    print(filmId[0])
    id = request.session['userid']
    user=models.AuthUser.objects.filter(id=id)
    clockFlag = False
    if(len(models.FilmWantSee.objects.filter(id_film_id=filmId[0].id, id_user_id=id))==0):
        print(0000000)
        filmWantSee=models.FilmWantSee(id_user=user[0], id_film=filmId[0])
        filmWantSee.save()
        clockFlag = True
    else:
        print(1111111)
        filmWantSee=models.FilmWantSee.objects.get(id_user=user[0], id_film=filmId[0])
        filmWantSee.delete()
        clockFlag=False

    # likes = models.FilmLike.objects.filter(id_film=filmId[0].id)

    # if (len(models.FilmLike.objects.filter(id_film_id=filmId[0].id, id_user_id=id)) != 0):


    film=[]
    # film.append(len(likes))
    film.append(clockFlag)
    return HttpResponse(json.dumps({'data': film}))

def WantSee(request):
    id=request.session['userid']
    name = request.session['username']
    # films=models.FilmLike.objects.filter(id_film_id=filmId[0].id, id_user_id=id)
    films=models.Film.objects.filter(filmwantsee__id_user=id).order_by('id')
    return render(request, 'Profile/WantSee.html', locals())

def AddFavorite(request):
    filmName = request.GET.get("filmName")
    filmName = filmName.strip()
    filmId=models.Film.objects.filter(name=filmName)
    print(filmId[0])
    id = request.session['userid']
    user=models.AuthUser.objects.filter(id=id)
    starFlag = False
    if(len(models.FilmFavorite.objects.filter(id_film_id=filmId[0].id, id_user_id=id))==0):
        print(0000000)
        filmFavorite=models.FilmFavorite(id_user=user[0], id_film=filmId[0])
        filmFavorite.save()
        starFlag = True
        album=models.Album.objects.filter(name="Избранное", id_user=id)
        filmAlbum=models.FilmAlbum(id_film=filmFavorite,id_album=album[0])
        filmAlbum.save()
    else:
        print(1111111)
        filmFavorite=models.FilmFavorite.objects.get(id_user=user[0], id_film=filmId[0])
        album = models.Album.objects.filter(name="Избранное", id_user=id)
        filmAlbum = models.FilmAlbum(id_film=filmFavorite, id_album=album[0])
        filmAlbum.delete()
        filmFavorite.delete()
        starFlag=False
    film=[]
    # film.append(len(likes))
    film.append(starFlag)
    return HttpResponse(json.dumps({'data': film}))

def Detail(request):
    id = request.session.get('userid', 'no')
    filmName = request.GET.get("filmName")
    if (id != 'no'):
        film = models.Film.objects.filter(name=filmName)
        name = request.session['username']
        likes = len(models.FilmLike.objects.filter(id_film=film[0].id))
        id = request.session['userid']
        likeFlag = False
        if (len(models.FilmLike.objects.filter(id_film=film[0].id, id_user=id)) != 0):
            likeFlag = True
        clockFlag = False
        if (len(models.FilmWantSee.objects.filter(id_film=film[0].id, id_user=id)) != 0):
            clockFlag = True
        starFlag = False
        if (len(models.FilmFavorite.objects.filter(id_film=film[0].id, id_user=id)) != 0):
            starFlag = True
        comments = models.FilmComment.objects.filter(id_film=film[0].id).order_by('-date_time')
        comment = []
        for c in comments:
            com = []
            com.append(c.id_user.first_name)
            com.append(c.date_time.strftime("%d-%m-%Y %H:%M"))
            com.append(c.text)
            comment.append(com)
        i=1
        rating=[]
        while(film[0].rating!=len(rating)):
            rating.append(i)
        i=0
        notrating=[]
        while(len(rating)+len(notrating)!=5):
            notrating.append(i)
        genres = models.FilmByGenre.objects.filter(id_film=film[0].id)
        genre = []
        for g in genres:
            genre.append(g.id_genre.name)
        countries = models.FilmByCountry.objects.filter(id_film=film[0].id)
        country = ''
        for i in range(0,len(countries)-1):
            country=country+countries[i].id_country.name+', '
        country = country + countries[len(countries)-1].id_country.name
        return render(request, 'Profile/Detail.html', locals())
    else:
        # return redirect('/Detail/', args={'filmName': filmName})
        return HttpResponseRedirect("/Detail/?filmName="+filmName)

def Exit(request):
    logout(request)
    return HttpResponseRedirect("/")


def Dev(request):
    name = request.session['username']
    return render(request, 'Profile/Dev.html', locals())


def Favorite(request):
    id=request.session['userid']
    name = request.session['username']
    film=models.Film.objects.filter(filmfavorite__id_user=id)

    return render(request, 'Profile/Favorite.html', locals())


def Last(request):
    id=request.session['userid']
    name = request.session['username']
    films=models.Film.objects.order_by('-filmlast__date').filter(filmlast__id_user=id)
    return render(request, 'Profile/Last.html', locals())


def Album(request):
    id = request.session.get('userid', 'no')
    name = request.session['username']
    album_name = models.Album.objects.filter(id_user=id)
    album=[]
    for a in album_name:
        film=[]
        film.append(a.name)
        films=models.Film.objects.filter(filmalbum__id_album=a.id)
        if(len(films)>4):
            fims=films[:4]
        album.append(film)
        album.append(films)
    return render(request, 'Profile/Album.html', locals())


def CheckAlbumName(request):
    albumName = request.GET.get("albumName")
    id = request.session['userid']
    albums=models.Album.objects.filter(name=albumName,id_user=id)
    flag=False
    print(len(albums))
    if(len(albums)==0):
        flag=True
    else:
        flag=False
    return HttpResponse(json.dumps({'data': flag}))


def AddAlbumAndFilm(request):
    albumName = request.GET.get("albumName")
    filmName = request.GET.get("filmName")
    print(filmName)
    id = request.session['userid']
    user=models.AuthUser.objects.filter(id=id)
    albums=models.Album(id_user=user[0], name=albumName)
    albums.save()
    print(albums)

    film = models.Film.objects.filter(name=filmName)
    print(film[0])
    filmAdd = models.FilmAlbum(id_album=albums, id_film=film[0])
    filmAdd.save()

    return HttpResponse(json.dumps({'data': 'ok'}))


def AddFilmInAlbum(request):
    albumName = request.GET.get("albumName")
    filmName = request.GET.get("filmName")
    print('element')
    id = request.session['userid']
    user=models.AuthUser.objects.filter(id=id)
    album=models.Album.objects.filter(id_user=id, name=albumName)
    print(filmName)
    film=models.Film.objects.filter(name=filmName)
    filmAdd=models.FilmAlbum(id_album=album[0],id_film=film[0])
    filmAdd.save()
    print(filmAdd)
    return HttpResponse(json.dumps({'data': 'ок'}))