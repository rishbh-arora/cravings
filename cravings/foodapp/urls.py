from django.urls import path
from . import views

urlpatterns = [
    path("", views.login),
    path("login", views.login),
    path("signup", views.signup),
    path("profile", views.profile),
    path("logout/", views.logout),
    path("messsignup", views.messsignup),
    
    path("menu", views.showmenu),
    path("invoice", views.invoice),
    path("user_home", views.user_home),
    path("about/", views.about),
    path("user_history", views.orderhistory),

    path("mess_orders", views.pending_orders),
    path("ready_orders", views.ready_orders),
    path("delivered_orders", views.delivered_orders),
    path("mess_home", views.mess_home),
    path("add_item", views.add_item),
    path("about_mess", views.about_mess),

    
    
]