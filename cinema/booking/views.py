from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Movie, BookingMovie, User, UserProfileInfo
from django.http import Http404
from .forms import BookingForm, UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    latest_movie_list = Movie.objects.order_by("-title")
    context = {
        "latest_movie_list": latest_movie_list,
    }
    return render(request, "booking/index.html", context)


@login_required
def new_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            movie_id = form.cleaned_data["movie_id"]
            name = form.cleaned_data["customer_name"]
            print(name)
            email = form.cleaned_data["customer_email"]
            pax = form.cleaned_data["pax"]

            # movie = Movie.objects.get(pk=movie_id)
            new_customer = BookingMovie(
                movie_id=movie_id, pax=pax, name=name, email=email
            )
            new_customer.save()
            return render(request, "booking/thanks.html")
    else:
        form = BookingForm()

    return render(request, "booking/new_booking.html", {"form": form})


@login_required
def detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        customer = BookingMovie.objects.filter(movie_id=movie_id).all()

    except Exception as e:
        raise Http404("Movie does not exist, error : {}".format(e))
    return render(
        request, "booking/details.html", {"customer": customer, "movie": movie}
    )


def show(request, movie_id):
    response = "You're looking at the movie %s."
    return HttpResponse(response % movie_id)


# Login
@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if "profile_pic" in request.FILES:
                print("found it")
                profile.profile_pic = request.FILES["profile_pic"]
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(
        request,
        "booking/registration.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "registered": registered,
        },
    )


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, "booking/login.html", {})

