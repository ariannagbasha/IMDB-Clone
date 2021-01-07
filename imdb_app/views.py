from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from imdb_app.forms import LoginForm, SignUpForm
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from imdb_app.models import IMDbUser
from django.template import RequestContext


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


def handler404(request, *args, **argv):
    context = {}
    response = render(None, '404.html', {},
                      context)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    context = {}
    response = render(None, '500.html', {},
                      context)
    response.status_code = 500
    return response
