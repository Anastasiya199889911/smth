from django.shortcuts import render, redirect
# rom smth import models
from . import models
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
import requests
import bs4
import random
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def Main(request):
    # потом убрать logout
    # logout(request)
    id = request.session.get('userid', 'no')
    if (id != 'no'):
        id = request.session['userid']
        name = request.session['username']
        # email = request.session['useremail']
        # return render(request, 'Profile/Profile.html', locals())
        return HttpResponseRedirect("/Profile")
    else:
        now = datetime.now().year
        film = models.Film.objects.order_by('-year').filter(year=now)

        filmsKount = models.Film.objects.order_by('-year').filter(year=now).count()

        films = models.Film.objects.order_by('-year').filter(year=now)[0:16]
        k = 0
        while (filmsKount > 0):
            k = k + 1
            filmsKount = filmsKount - 16
        ListPage = []
        page = 1
        if (k > 6):
            for i in range(1, 4):
                ListPage.append(i)
            ListPage.append('...')
            for i in range(k - 2, k + 1):
                ListPage.append(i)
        else:
            for i in range(1, k + 1):
                ListPage.append(i)
        pre = 1
        next = page + 1

        return render(request, 'Main/Main.html', locals())
    # logout(request)
    # return render(request, 'Main/Main.html', locals())


def Main_Page(request):
    page = int(request.GET.get("page"))
    start=page*16-16
    end=page*16
    now = datetime.now().year
    film = models.Film.objects.all().order_by('-year').filter(year=now)
    filmsKount = models.Film.objects.order_by('-year').filter(year=now).count()

    films = models.Film.objects.order_by('-year').filter(year=now)[start:end]

    k =0
    while (filmsKount > 0):
        k = k + 1
        filmsKount = filmsKount - 16
    Page = []
    if k>6:
        # записать первые 3
        for i in range(1,4):
            Page.append(i)
        # записать середину
        if page >= 3 and page <= (k - 2):
            for i in range(page - 1, page + 2):
                Page.append(i)
        # записать последние 3
        for i in range(k - 2, k+1):
            Page.append(i)
    else:
        for i in range(1,k+1):
            Page.append(i)
    # убрать повторения
    Page = list(set(Page))
    ListPage = []
    # добавить '...'
    for i in range(len(Page) - 1):
        ListPage.append(Page[i])
        if Page[i + 1] - Page[i] > 1:
            ListPage.append('...')
    ListPage.append(Page[len(Page) - 1])
    pre = page-1
    next = page+1
    return render(request, 'Main/Main.html', locals())


def Parse(request):
    # selectElementsAboutFilm=["Оригинальное название", "Жанр", "Год", "Страна", "Продолжительность", "Режиссер"]
    # 12 мюзикл
    genres = models.Genre.objects.all()
    g0=[1]
    # print(g0)
    for g_0 in g0:
        print(g_0)
        g=genres[g_0]
        print(g.name)
        # for g in genres:
        pageCount=g.pages
        way=g.way
        for i in range(736,pageCount+1):
            print(i)
            url = requests.get(way + str(i) + '/')
            print(way + str(i) + '/')
            url.encoding = 'utf8'
            b = bs4.BeautifulSoup(url.text, "html.parser")
            name = b.select('.shorbox .shorposterbox .postertitle h2 a')
            for n in name:
                print(n.getText())
                fi=models.Film.objects.filter(name=n.getText())
                # print(fi.name)
                if(len(fi)==0):
                    # print(fi.name)
                    list_genre=[]
                    list_country=[]
                    film=models.Film()
                    film.url=n.get('href')
                    film.name=n.getText()
                    print(n.getText())
                    url2=requests.get(n.get('href'))
                    url2.encoding = 'utf8'
                    b2 = bs4.BeautifulSoup(url2.text, "html.parser")
                    image = b2.select('.fullbox .leftfull .bigposter img')
                    for i in image:
                        film.image=i.get('src')
                    information = b2.select('.fullbox .fullright .janrfall li')
                    for i in information:
                        if(i.getText().find("Оригинальное название")!=-1):
                            film.original_name=(i.getText()).split(": ")[1]
                        if (i.getText().find("Год:") != -1):
                            print(i.getText().split(": "))
                            film.year=int((i.getText()).split(": ")[1])
                        if (i.getText().find("Продолжительность") != -1):
                            film.duration=(i.getText()).split(": ")[1]
                        if (i.getText().find("Режиссёр") != -1):
                            film.producer=(i.getText()).split(": ")[1]
                        if (i.getText().find("Жанр") != -1):
                            g=(i.getText()).split(": ")[1]
                            list_genre=g.split(", ")
                        if (i.getText().find("Страна") != -1):
                            c=(i.getText()).split(":")[1]
                            list_country=c.split(", ")
                    rating = b2.select('.fullbox .fullright .rating-more b')
                    for r in rating:
                        film.rating=int(round(int(round(float((r.getText()).split(": ")[1])))/2))
                    text = b2.select('.fulltext')
                    for t in text:
                        film.text=t.getText()
                    film.save()

                    for g in list_genre:
                        gg=g.capitalize()
                        ge=models.Genre.objects.filter(name=gg)
                        if(len(ge)>0):
                            film_by_genre = models.FilmByGenre()
                            film_by_genre.id_genre=ge[0]
                            film_by_genre.id_film=film
                            film_by_genre.save()

                    for c in list_country:
                        c=c.strip()
                        cc = models.Country.objects.filter(name=c)
                        if (len(cc) > 0):
                            film_by_country = models.FilmByCountry()
                            film_by_country.id_country = cc[0]
                            film_by_country.id_film = film
                            film_by_country.save()
                        else:
                            country=models.Country()
                            country.name=c
                            country.save()
                            film_by_country = models.FilmByCountry()
                            film_by_country.id_country = country
                            film_by_country.id_film = film
                            film_by_country.save()
                else:
                    print('уже есть!!!')
    return render(request, 'Main/Main.html', locals())


def RandomSearch(request):
    id = request.session.get('userid', 'no')
    if (id != 'no'):
        id = request.session['userid']
        name = request.session['username']
        # email = request.session['useremail']
        # return render(request, 'Profile/Ra.html', locals())
        return HttpResponseRedirect("/Profile/SearchByRandom")
    else:
        return render(request, 'Main/RandomSearch.html', locals())


def Random_SearchFilm(request):
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
    return HttpResponse(json.dumps({'data': film}))


def Registration(request):
    return render(request, 'Main/Registration.html', locals())


def SearchByCategory(request):
    genres=models.Genre.objects.all()
    years=models.Year.objects.all()
    countries=models.Country.objects.all()
    ratings=models.Rating.objects.all()
    return render(request, 'Main/SearchByCategory.html', locals())


def Category_SearchFilm(request):
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
    return HttpResponse(json.dumps({'data': film}))


def Registrate(request):
    name = request.GET.get("name")
    email = request.GET.get("email")
    password = request.GET.get("pass1")
    user=User.objects.create_user(email, email, password)
    user.first_name = name
    # user=models.User(name=name,login=email,password=password)
    user.save()
    auth_user=models.AuthUser.objects.filter(id=user.id)
    # album=models.Album(id_user=auth_user[0], name="Избранное")
    # album.save()
    return HttpResponse(json.dumps({'data': ''}))

def Authorization(request):
    return render(request, 'Main/Authorization.html', locals())


def Authorize(request):
    email = request.GET.get("email")
    passw = request.GET.get("passw")
    user = authenticate(username=email, password=passw)

    if user is None:
        return HttpResponse(json.dumps({'data': 'false'}))
    else:
        login(request,user)
        request.session['userid']=user.id
        # request.session['useremail'] = user.username
        request.session['username'] = user.first_name
        request.session.modified = True
        return HttpResponse(json.dumps({'data': 'true'}))

def Detail(request):
    filmName=request.GET.get('filmName')
    film = models.Film.objects.filter(name=filmName)
    likes = len(models.FilmLike.objects.filter(id_film=film[0].id))
    i = 1
    rating = []
    while (film[0].rating != len(rating)):
        rating.append(i)
    i = 0
    notrating = []
    while (len(rating) + len(notrating) != 5):
        notrating.append(i)
    genres = models.FilmByGenre.objects.filter(id_film=film[0].id)
    genre = []
    for g in genres:
        genre.append(g.id_genre.name)
    countries = models.FilmByCountry.objects.filter(id_film=film[0].id)
    country = ''
    for i in range(0, len(countries) - 1):
        country = country + countries[i].id_country.name + ', '
    country = country + countries[len(countries) - 1].id_country.name
    return render(request, 'Main/Detail.html', locals())


def AlbumInfo(request):
    albumName=request.GET.get('albumName')
    params = albumName.split('|')
    album_name=params[0]
    id=params[1]
    albums = models.Album.objects.filter(id_user=id, name=album_name)
    films = models.Film.objects.filter(filmalbum__id_album=albums[0].id)
    # name = request.session['username']
    return render(request, 'Main/AlbumInfo.html', locals())