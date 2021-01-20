from django.db import models
from django.contrib.auth.models import AbstractUser

from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


class IMDbUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254)
    seen_movies = models.ManyToManyField(
        "Movie",
        blank=True,
        symmetrical=False,
        related_name='seen_movies'
    )
    want_list_movies = models.ManyToManyField(
        "Movie",
        blank=True,
        symmetrical=False,
        related_name='want_list_movies'
    )

    recently_viewed = models.ManyToManyField(
        "History",
        blank=True,
        symmetrical=False,
        related_name='recently_viewed'
    )

    def __str__(self):
        return self.username


class History(models.Model):
    title = models.CharField(max_length=350)
    movie_id = models.IntegerField(blank=True, null=True)
    image = models.URLField(max_length=1000)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=350)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    counting = models.IntegerField()
    crew = models.CharField(max_length=1000)
    image = models.URLField(max_length=1000)

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author = models.ForeignKey(IMDbUser, on_delete=models.CASCADE)
    stars = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} - ({self.stars})'