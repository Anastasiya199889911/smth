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
