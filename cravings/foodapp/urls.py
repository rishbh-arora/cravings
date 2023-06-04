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
    path("mess_orders", views.mess),
    path("add_item", views.add_item),
    path("user_home", views.user_home),
    path("about", views.about),
    path("user_history", views.orderhistory),
    path("about_mess", views.about_mess),
]