from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("login/logging", views.login_auth, name="login-auth"),
    path("login/signing", views.signup_auth, name="signup-auth"),
    path("logout/", views.logout_view, name="logout")

]