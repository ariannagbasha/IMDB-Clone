from django import forms
from django.contrib.auth.forms import UserCreationForm
from imdb_app.models import IMDbUser, Movie
from django.core.validators import MaxValueValidator, MinValueValidator

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150,)
    first_name = forms.CharField(max_length=350, required=True)
    last_name = forms.CharField(max_length=350, required=True)
    email = forms.CharField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class ReviewForm(forms.Form):
    title = forms.CharField(max_length=50)
    stars = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])




