from django.urls import path
from . import views
urlpatterns = [
    path(r'', views.index),
    path(r'/purchase_property', views.showProperties),
    path(r'/purchase_history', views.bookedDashboard),
    path(r'/properties_history', views.showPropertyDashboard),
    path(r'/add_property', views.showPropertyForm),
    path(r'/listProperty', views.addProprty),
    path(r'/bookProperty/<int:id>/', views.bookProperty),
    path(r'/buyProperty/<int:id>/', views.buyProperty),
]