from django import forms
from .models import Movie, BookingMovie, UserProfileInfo
from django.contrib.auth.models import User


class BookingForm(forms.Form):
    customer_name = forms.CharField(label="Your Name")
    customer_email = forms.CharField(label="Your Email")
    pax = forms.IntegerField(label="Pax")
    movie_id = forms.ModelChoiceField(queryset=Movie.objects.all())


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password", "email")


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ("portfolio_site", "profile_pic")

