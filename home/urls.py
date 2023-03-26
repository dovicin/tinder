from django import http, views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_form),
    path("index", views.index),
    path("index.html", views.index),
    path("homepage.html", views.index),
    path("index2", views.index2),
    path("index2.html", views.index2),
    path("homepage2.html", views.index2),
    path("profilepage.html", views.profile),
    path("cards.html", views.cards),
    path("login.html", views.login_form, name='login.html'),
    path("login", views.login_form, name='login.html'),
    path("signup.html", views.join_form, name='signup.html'),
    path("logout.html", views.logout, name='logout.html'),
    path("otp.html", views.otp),
    path("heart.html", views.heart),

]