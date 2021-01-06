from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db.models import Model

# Create your models here.


class IMDbUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField((""), max_length=254)
    seenmovies = models.ManyToManyField(
        "self",
        related_name="users_movies",
        symmetrical=False
    )
    wanttosee = models.ManyToManyField(
        "self",
        related_name="must_see_movies",
        symmetrical=False,
    )


class Movie(models.Model):
    title = models.CharField(max_length=350)
    rating = models.FloatField(null=True, default=5)
    crew = models.CharField(max_length=50)
    image = models.URLField(max_length=200)


class Review(models.Model):
    title = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
