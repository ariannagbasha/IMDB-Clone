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
from django.urls import path, include
from imdb_app import views
from django.conf.urls import handler404, handler500, url
from imdb_app import views as imdb_app_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.Index.as_view(), name="homepage"),
    path("admin/", admin.site.urls),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("sign_up/", views.SignUp.as_view(), name="sign_up"),
    path('error_500', views.error_500, name='data'),
    path('error_404', views.error_404, name='data'),
    path("movie_detail/<int:movie_id>/", views.movie_detail, name="movie_detail"),
    path("reviews/<int:movie_id>/", views.review_submission, name="review"),
    path("search/<search_query>/", views.search_results_view, name="search_results")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
