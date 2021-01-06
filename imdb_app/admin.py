
from django.contrib import admin
from imdb_app.models import Movie, Review, IMDbUser

<<<<<<< HEAD
# Register your models here.
admin.site.register(Movie, Review)
admin.site.register(IMDbUser)
=======
models = [Movie, Review, IMDbUser]
admin.site.register(models)

>>>>>>> 5817dffdbd006e1cadaed20e6f700c201032d9aa
