from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.RandomSearch, name="RandomSearch"),
    url(r'SearchFilm', views.SearchFilm, name="SearchFilm"),
]