from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Main, name="Main"),
    url(r'^RandomSearch/', views.RandomSearch, name="RandomSearch"),
    url(r'/Random_SearchFilm', views.Random_SearchFilm, name="Random_SearchFilm"),

    url(r'^SearchByCategory/', views.SearchByCategory, name="SearchByCategory"),
    url(r'/Category_SearchFilm', views.Category_SearchFilm, name="Category_SearchFilm"),


    url(r'^/Parse/', views.Parse, name="Parse"),
    url(r'^Registration/', views.Registration, name="Registration"),
    url(r'/Registrate', views.Registrate, name="Registrate"),
    url(r'^Authorization/', views.Authorization, name="Authorization"),
    url(r'/Authorize', views.Authorize, name="Authorize"),
]