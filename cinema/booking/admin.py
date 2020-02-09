from django.contrib import admin
from .models import Movie, BookingMovie, UserProfileInfo, User

admin.site.register(Movie)
admin.site.register(BookingMovie)
admin.site.register(UserProfileInfo)