from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from imdb_app.forms import LoginForm, SignUpForm, ReviewForm
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from imdb_app.models import IMDbUser, Movie, Review


class Index(View):
    def get(self, request):
        return render(
            request,
            "index.html",)


class LoginView(TemplateView):
    def post(self, request):

        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
        login(request, user)
        return HttpResponseRedirect(request.GET.get("next", reverse("homepage")))

    def get(self, request):
        form = LoginForm()

        return render(request, "generic_form.html", {"form": form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


class SignUp(LoginRequiredMixin, View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "generic_form.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newuser = IMDbUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
            )
            login(request, newuser)
            return HttpResponseRedirect(reverse("homepage"))

def movie_detail(request, movie_id):
    html = "movie_detail.html"
    get_movie = Movie.objects.get(id=movie_id)
    movie_reviews = Review.objects.filter(movie=get_movie)
    return render(request, html, {"movie": get_movie, "reviews": movie_reviews})


def review_submission(request, movie_id):
    html = "generic_form.html"
    get_movie = Movie.objects.get(id=movie_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_review = Review.objects.create(
                title=data['title'],
                movie=get_movie,
                author=request.user,
                stars=data['stars']
            )
            new_review.save()
            get_movie.counting += 1
            sum_total_of_rating = get_movie.counting * get_movie.rating
            print(sum_total_of_rating)
            get_movie.rating = round((sum_total_of_rating + new_review.stars) / get_movie.counting, 1)
            get_movie.save()
            return HttpResponseRedirect(reverse("homepage"))
    form = ReviewForm()
    return render(request, html, {'form': form})
