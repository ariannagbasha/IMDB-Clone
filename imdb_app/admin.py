
from django.contrib import admin
from imdb_app.models import Movie, Review, IMDbUser

models = [Movie, Review, IMDbUser]
admin.site.register(models)

