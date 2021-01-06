
from django.contrib import admin
from imdb_app.models import Movie, Review, IMDbUser


admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(IMDbUser)

