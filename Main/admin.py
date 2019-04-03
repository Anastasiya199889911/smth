from django.contrib import admin
from .models import *

# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Country._meta.fields]

    class Meta:
        model = Country

admin.site.register(Country, CountryAdmin)


class FilmAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Film._meta.fields]

    class Meta:
        model = Film

admin.site.register(Film, FilmAdmin)


class FilmByCountryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FilmByCountry._meta.fields]

    class Meta:
        model = FilmByCountry

admin.site.register(FilmByCountry, FilmByCountryAdmin)


class FilmByGenreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FilmByGenre._meta.fields]

    class Meta:
        model = FilmByGenre

admin.site.register(FilmByGenre, FilmByGenreAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Genre._meta.fields]

    class Meta:
        model = Genre

admin.site.register(Genre, GenreAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Rating._meta.fields]

    class Meta:
        model = Rating

admin.site.register(Rating, RatingAdmin)


class YearAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Year._meta.fields]

    class Meta:
        model = Year

admin.site.register(Year, YearAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]

    class Meta:
        model = User

admin.site.register(User, UserAdmin)