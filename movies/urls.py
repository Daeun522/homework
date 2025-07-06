from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:pk>/rate/', views.movie_rate, name='movie_rate'),
    path('movie/<int:pk>/result/', views.movie_result, name='movie_result'),
]
