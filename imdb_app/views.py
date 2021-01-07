from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from imdb_app.forms import LoginForm, SignUpForm
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from imdb_app.models import IMDbUser, Movie


class Index(View):
    def get(self, request):             
        html = 'index.html'
        context = {}
        return render(request, html, context)

class Movies(View):
    def get(self, request):
        movies = Movie.objects.all().order_by('title')
        html = 'movies.html'
        context = {'movies': movies}
        return render(request, html, context)

@login_required
def seen_list(request, movie_id):
    user = IMDbUser.objects.get(id=request.user.id)
    movie = Movie.objects.get(id=movie_id)
    user.seen_movies.add(movie)
    user.save()
    return redirect('/movies/')

@login_required
def watchlist(request, movie_id):
    user = IMDbUser.objects.get(id=request.user.id)
    movie = Movie.objects.get(id=movie_id)
    user.want_list_movies.add(movie)
    user.save()
    return redirect('/movies/')

class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = IMDbUser.objects.get(id=user_id)
        seen_movies = user.seen_movies.all()
        want_list_movies = user.want_list_movies.all()               
        html = 'profile.html'
        context = {
            'user': user,
            'seen_movies': seen_movies,
            'want_list_movies': want_list_movies}
        return render(request, html, context)

class LoginView(TemplateView):
    form_class = LoginForm
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(
                request, username=username, password=password
            )            
            if user or request.user.is_superuser:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", reverse("homepage")))
            else:
                return redirect('/login/')

    def get(self, request):
        form = self.form_class()
        html = 'generic_form.html'
        context = {'form': form}

        return render(request, html, context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


class SignUp(View):
    form_class = SignUpForm
    def get(self, request):
        form = self.form_class()
        html = 'generic_form.html'
        context = {'form': form}
        return render(request, html, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            newuser = IMDbUser.objects.create_user(
                username=username,
                password=password,
            )
            if newuser:
                login(request, newuser)
            return HttpResponseRedirect(reverse("homepage"))

