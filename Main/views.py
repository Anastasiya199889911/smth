from django.shortcuts import render
# rom smth import models
from . import models
from django.http import HttpResponse, JsonResponse
import json
import requests
import bs4

# Create your views here.


def Main(request):
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


def Registration(request):
    return render(request, 'Main/Registration.html', locals())


def Registrate(request):
    name = request.GET.get("name")
    email = request.GET.get("email")
    password = request.GET.get("pass1")
    user=models.User(name=name,login=email,password=password)
    user.save()
    # return render(request, 'Main/Main.html', locals())
    return HttpResponse(json.dumps({'data': ''}))

def Authorization(request):
    return render(request, 'Main/Main.html', locals())