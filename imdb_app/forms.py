from django import forms
from django.contrib.auth.forms import UserCreationForm
from imdb_app.models import IMDbUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = IMDbUser
        fields = [
            "first_name",
            "last_name",
        ]
