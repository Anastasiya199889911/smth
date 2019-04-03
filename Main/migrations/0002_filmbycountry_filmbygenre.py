# Generated by Django 2.1.5 on 2019-04-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmByCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'film_by_country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmByGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'film_by_genre',
                'managed': False,
            },
        ),
    ]
