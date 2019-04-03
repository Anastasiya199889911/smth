from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Main, name="Main"),
    url(r'Parse', views.Parse, name="Parse"),
    url(r'Registration', views.Registration, name="Registration"),
    url(r'Registrate', views.Registrate, name="Registrate"),
    url(r'Authorization', views.Authorization, name="Authorization"),
]