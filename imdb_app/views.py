from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from imdb_app.forms import LoginForm, SignUpForm, ReviewForm
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from imdb_app.models import IMDbUser, Movie, Review, History
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm 



class Index(View):
    def get(self, request):
        html = 'index.html'
        image = '../media/images/1-10.png'
        recently_viewed = []
        watchlist = ''
        if request.user.is_authenticated:
            user = IMDbUser.objects.get(id=request.user.id)
            recently_viewed = user.recently_viewed.all().order_by('-id')[:10]
            watchlist = user.want_list_movies.all()                                  
        top_ten_movies = Movie.objects.all().order_by('id')[:10]
        random_movies = Movie.objects.all().order_by('?')[:20]
        context = {'image': image, 'movies': top_ten_movies, 'watchlist': watchlist, 'random': random_movies, 'recently_viewed': recently_viewed}
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
    return redirect(f'/movie_detail/{movie_id}/')

@login_required
def watchlist(request, movie_id):
    user = IMDbUser.objects.get(id=request.user.id)
    movie = Movie.objects.get(id=movie_id)
    user.want_list_movies.add(movie)
    user.save()
    return redirect(f'/movie_detail/{movie_id}/')

class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = IMDbUser.objects.get(id=user_id)          
        recently_viewed = user.recently_viewed.all().order_by('-id')[:10]          
        seen_movies = user.seen_movies.all()
        want_list_movies = user.want_list_movies.all()               
        html = 'profile.html'
        context = {
            'user': user,
            'seen_movies': seen_movies,
            'want_list_movies': want_list_movies,
            'recently_viewed': recently_viewed
        }
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
        html = 'login.html'
        context = {'form': form}

        return render(request, html, context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


class SignUp(View):
    form_class = SignUpForm
    def get(self, request):
        form = self.form_class()
        html = 'sign_up.html'
        context = {'form': form}
        return render(request, html, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            email = data['email']
            first_name = data['first_name']
            last_name = data['last_name']
            password = data['password']
            newuser = IMDbUser.objects.create_user(
                username=username,
                email = email,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
            if newuser:
                login(request, newuser)
            return HttpResponseRedirect(reverse("success"))

def sign_up_success(request):
    html = 'success.html'
    context = {}
    return render(request, html, context)

def handler404(request, *args, **argv):
    context = {}
    response = render(None, '404.html',
                      context)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    context = {}
    response = render(None, '500.html',
                      context)
    response.status_code = 500
    return response

def movie_detail(request, movie_id):
    html = "movie_detail.html"    
    movie = Movie.objects.get(id=movie_id)    
    if request.user.is_authenticated:
        user = IMDbUser.objects.get(id=request.user.id)
        ids = list(History.objects.all().values_list('movie_id', flat=True))               
        if movie_id not in ids:       
            hist_obj = History.objects.create(
            title = movie.title,
            movie_id = movie_id,
            image = movie.image
            )
            user.recently_viewed.add(hist_obj)
            user.save()
        else:           
            hist_obj = History.objects.get(movie_id=movie_id)            
            user.recently_viewed.remove(hist_obj)
            user.save()
            hist_obj.delete()          

            hist_obj = History.objects.create(
            title = movie.title,
            movie_id = movie_id,
            image = movie.image
            )
            user.recently_viewed.add(hist_obj)
            user.save()  

    # reviews = Review.objects.filter(movie=movie)
    context = {"movie": movie}
    return render(request, html, context)


# def review_submission(request, movie_id):
#     html = "generic_form.html"
#     get_movie = Movie.objects.get(id=movie_id)
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_review = Review.objects.create(
#                 title=data['title'],
#                 movie=get_movie,
#                 author=request.user,
#                 stars=data['stars']
#             )
#             new_review.save()
#             get_movie.counting += 1
#             sum_total_of_rating = get_movie.counting * get_movie.rating
#             print(sum_total_of_rating)
#             get_movie.rating = round((sum_total_of_rating + new_review.stars) / get_movie.counting, 1)
#             get_movie.save()
#             return HttpResponseRedirect(reverse("homepage"))
#     form = ReviewForm()
#     context = {'form': form}
#     return render(request, html, context)

class SearchFormView(View):
    def get(self, request):
        html = 'search_form.html'
        context = {}
        return render(request, html, context)

class SearchResultsView(View):
    def get(self, request):             
        html = 'search_results.html'
        search_query = self.request.GET.get('q')
        results = Movie.objects.filter(
            Q(title__icontains=search_query) | Q(crew__icontains=search_query)
        )
        context = {'results': results, 'search_query': search_query}
        return render(request, html, context)
        
def SearchFormAutocomplete(request):
    html = 'search_form.html'
    if 'term' in request.GET:
        qs = Movie.objects.filter(title__icontains=request.GET.get('term'))
        titles = list()
        for movie in qs:
            titles.append(movie.title)
        return JsonResponse(titles, safe=False)
    return render(request, html)
