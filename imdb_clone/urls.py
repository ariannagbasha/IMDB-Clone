"""imdb_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from imdb_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Index.as_view(), name="homepage"),
    path('movies/', views.Movies.as_view(), name='movies'),
    path('user/<int:user_id>/', views.UserProfileView.as_view(), name='profile'),
    path('seen/<int:movie_id>/', views.seen_list, name='seen'),
    path('watchlist/<int:movie_id>/', views.watchlist, name='watchlist'),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("sign_up/", views.SignUp.as_view(), name="sign_up"),
]
