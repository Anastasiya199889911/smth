from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Profile, name="Profile"),
    url(r'^RandomSearch/', views.RandomSearch, name="Profile_RandomSearch"),
    url(r'Profile_Random_SearchFilm', views.Profile_Random_SearchFilm, name="Profile_Random_SearchFilm"),
    url(r'^SearchByCategory/', views.SearchByCategory, name="Profile_SearchByCategory"),
    url(r'Profile_Category_SearchFilm', views.Profile_Category_SearchFilm, name="Profile_Category_SearchFilm"),
    url(r'AddLike', views.AddLike, name="AddLike"),
    url(r'^Liked/', views.Liked, name="Liked"),
    url(r'AddComment', views.AddComment, name="AddComment"),
    url(r'AddWantSee', views.AddWantSee, name="AddWantSee"),
    url(r'^WantSee/', views.WantSee, name="WantSee"),
    url(r'AddFavorite', views.AddFavorite, name="AddFavorite"),
    url(r'^Detail/', views.Detail, name="Detail"),
    url(r'^Favorite/', views.Favorite, name="Favorite"),
    url(r'^Last/', views.Last, name="Last"),
    # url(r'Random_SearchFilm', views.Random_SearchFilm, name="Profile_Random_SearchFilm"),

    # url(r'SearchByCategory', views.SearchByCategory, name="Profile_SearchByCategory"),
    # url(r'Category_SearchFilm', views.Category_SearchFilm, name="Category_SearchFilm"),

    # url(r'SearchByCategory', views.SearchByCategory, name="ProfileSearchByCategory"),

    # url(r'^/Detail/', views.News_Story_Detail, name="News_Story_Detail"),
    url(r'^/Exit/', views.Exit, name="Exit"),
    url(r'^/Dev/', views.Dev, name="Dev"),
]