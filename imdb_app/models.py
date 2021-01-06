from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db.models import Model


class IMDbUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField((""), max_length=254)  
    seen_movies = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
    )
    want_to_see = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
    )

class Movie(models.Model):
    title = models.CharField(max_length=350)
    rating = models.FloatField((""))
    cast = models.CharField((""))
    image = models.URLField((""))


class Review(models.Model):
    title = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
