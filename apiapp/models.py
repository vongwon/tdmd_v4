from django.db import models


class Movie(models.Model):
    movieid = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=30)
    year = models.CharField(max_length=4, blank=True)
    length = models.CharField(max_length=10, blank=True)
    genres = models.CharField(max_length=100, blank=True)
    rate = models.IntegerField(default=0, blank=True)
    poster = models.URLField(default='', blank=True)
    plot = models.CharField(max_length=500, blank=True)
    trailer = models.URLField(default='', blank=True)

    def __str__(self):
        return self.movieid + '|' + self.title

    @staticmethod
    def get_name():
        return 'movie'


class Actor(models.Model):
    actorid = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=30)
    photo = models.URLField()

    def __str__(self):
        return self.actorid + '|' + self.name

    @staticmethod
    def get_name():
        return 'actor'

class ApiSearch(models.Model):
    api_query = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.api_query

class AllGenres(models.Model):
    genre_tmdb_id = models.CharField(max_length=10,blank=True, null=True)
    genre_name = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.genre_name

