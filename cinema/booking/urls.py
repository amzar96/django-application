from django.urls import path
from django.conf.urls import url

from . import views

app_name = "booking"
urlpatterns = [
    path("", views.index, name="index"),
    path("customer_booking/<int:movie_id>/", views.detail, name="details"),
    path("<int:movie_id>/show/", views.show, name="show"),
    path("new_booking/", views.new_booking, name="new_booking"),
    url(r"^register/$", views.register, name="register"),
    url(r"^user_login/$", views.user_login, name="user_login"),
]
