
from django.contrib import admin
from imdb_app.models import Movie, Review, IMDbUser, History


admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(IMDbUser)
admin.site.register(History)

