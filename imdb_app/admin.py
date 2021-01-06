
from django.contrib import admin
from imdb_app.models import Movie, Review, IMDbUser

models = [Movie, Review, IMDBUser]
admin.site.register(models)

