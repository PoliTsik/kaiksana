from django.db import models
from django.conf import settings
from django.utils import timezone


class Actor(models.Model):
    name = models.CharField(max_length=100)


class MovieType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()
    biography = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Movie(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    movie_type = models.ForeignKey(MovieType, on_delete=models.CASCADE)
    release_date = models.DateField(null=True, blank=True)
    imdb_url = models.URLField()
    image = models.ImageField(upload_to='media/', null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    stars = models.ManyToManyField(Actor)
    imdb_rating = models.FloatField()
    my_rating = models.FloatField()
    summary = models.TextField()

    def __str__(self):
        return self.title


# Create your models here.
