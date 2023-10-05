from django.urls import path

from .views import ListMovie, DetailMovie

urlpatterns = [
    path('<int:pk>/', DetailMovie.as_view(), name='movie_detail'),
    path('', ListMovie.as_view(), name='movie_list'),
]