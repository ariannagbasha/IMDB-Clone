from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class IMDbUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(_(""), max_length=254)
    seen_movies = models.ManyToManyField(
        "Movie",
        blank=True,
        symmetrical=False,
    )
    want_list_movies = models.ManyToManyField(
        "Movie",
        blank=True,
        symmetrical=False,
    )
class Movie(models.Model):
    title = models.CharField(max_length=350)
    rating = models.FloatField(_(""))
    crew = models.CharField(_(""))
    image = models.URLField(_(""))

class Review(models.Model):
    title = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)





