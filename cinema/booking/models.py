from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Movie(models.Model):
    title = models.CharField("Movie Title", max_length=200)
    price = models.FloatField("Price (RM)", default="0")
    show_date = models.DateTimeField("Movie Date")

    def __str__(self):
        return self.title


class BookingMovie(models.Model):
    movie_id = models.ForeignKey(
        Movie, related_name="movie_name", on_delete=models.CASCADE
    )
    pax = models.FloatField("Pax")
    name = models.CharField("Customer Name", max_length=200)
    email = models.CharField("Customer Email", max_length=200)

    def __str__(self):
        return self.name


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username
