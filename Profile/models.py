from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'country'


class Film(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    original_name = models.CharField(max_length=200, blank=True, null=True)
    year = models.IntegerField()
    duration = models.CharField(max_length=20)
    producer = models.CharField(max_length=200, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film'


class FilmByCountry(models.Model):
    id_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='id_country')
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film')

    class Meta:
        managed = False
        db_table = 'film_by_country'


class FilmByGenre(models.Model):
    id_genre = models.ForeignKey('Genre', models.DO_NOTHING, db_column='id_genre')
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film')

    class Meta:
        managed = False
        db_table = 'film_by_genre'


class Genre(models.Model):
    name = models.CharField(max_length=50)
    way = models.CharField(max_length=50)
    pages = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'genre'


class Rating(models.Model):
    name = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rating'


class Year(models.Model):
    name = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'year'




class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class FilmLike(models.Model):
    id_film = models.ForeignKey(Film, models.DO_NOTHING, db_column='id_film')
    id_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'film_like'