from django.urls import path
from . import views
urlpatterns = [
    path(r'', views.index),
    path(r'registration', views.registrationForm),
    path(r'register', views.register),
    path(r'login', views.login),
    path(r'logout', views.logoutView)
]