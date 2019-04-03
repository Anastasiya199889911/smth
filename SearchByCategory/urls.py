from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.SearchByCategory, name="SearchByCategory"),
    url(r'SearchFilm', views.SearchFilm, name="SearchFilm"),
]