from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import Template

def login_view(request):
    
    return render(request, "blog/login.html")

def login_auth(request):
    username = request.POST["login-username"]
    password = request.POST["login-password"]
    user = authenticate(request=request, username=username, password=password)
    
    if user != None:
        login(request, user)
    else:
        error_message = "Invalid username or password."
        context = { "error_message": error_message }
        return render(request, "blog/login.html", context)

    return HttpResponseRedirect(reverse("blog:home"))

def signup_auth(request):
    email = request.POST["signup-email"]
    username = request.POST["signup-username"]
    password = request.POST["signup-password"]
    password2 = request.POST["signup-password2"]

    if password == password2:
        current_user = User.objects.create_user(email=email, username=username, password=password)

    return HttpResponseRedirect(reverse("blog:home"))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("blog:login"))


def home(request):
    # FIGURE OUT PERSISTANCE
    if request.user.is_authenticated:
        return render(request, "blog/home.html")
    else:
        return HttpResponse("You need to log in to see this page!")