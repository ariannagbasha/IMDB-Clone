from django.contrib import admin
from imdb_app.models import IMDbUser
from django.contrib.auth.admin import UserAdmin


admin.site.register(IMDbUser, UserAdmin)
