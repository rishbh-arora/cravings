from django.urls import path
from . import views

urlpatterns = [
    path("", views.login),
    path("login", views.login),
    path("signup", views.signup),
    path("profile", views.profile),
    path("mess", views.mess),
    path("menu", views.showmenu),
    path("logout", views.logout),
    path("invoice", views.invoice),
    path("messsignup", views.messsignup),
    path("mess_home", views.mess_home),
    path("add_item", views.add_item),
]