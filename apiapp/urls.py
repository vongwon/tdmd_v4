from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('moviedetails/', views.moviedetails, name='moviedetails'),
    path('genre/', views.addgenre, name='genre')
]
