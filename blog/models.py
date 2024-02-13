from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Actor(models.Model):
    name = models.CharField(max_length=100)
    GENDER_CHOICES = (('M', 'Άνδρας'), ('F', 'Γυναίκα'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    awarded = models.BooleanField(default=False)
    def __str__(self):
        return self.name

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
    duration = models.IntegerField(validators=[MinValueValidator(10),MaxValueValidator(300),])
    movie_type = models.ForeignKey(MovieType, on_delete=models.CASCADE)
    release_date = models.DateField(null=True, blank=True)
    imdb_url = models.URLField()
    image = models.ImageField(upload_to='media/', null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    stars = models.ManyToManyField(Actor)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0),MaxValueValidator(10.0)])
    my_rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0),MaxValueValidator(10)])
    summary = models.TextField()
    user_rating = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.title


# Create your models here.
