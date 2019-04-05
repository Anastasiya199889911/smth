from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Profile, name="Profile"),

    url(r'RandomSearch', views.RandomSearch, name="RandomSearch"),
    url(r'Random_SearchFilm', views.Random_SearchFilm, name="Random_SearchFilm"),

    url(r'SearchByCategory', views.SearchByCategory, name="SearchByCategory"),
    url(r'Category_SearchFilm', views.Category_SearchFilm, name="Category_SearchFilm"),

    url(r'Exit', views.Exit, name="Exit"),
]