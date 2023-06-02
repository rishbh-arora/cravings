from django.urls import path
from . import views

urlpatterns = [
    path("", views.login),
    path("login", views.login),
    path("signup", views.signup),
    path("profile", views.profile),
    path("mess", views.mess),
    path("menu", views.menu),
    path("place_order", views.place_order)
]