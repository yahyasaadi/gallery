from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-photo'),
    path('search/', views.search, name='search')
]