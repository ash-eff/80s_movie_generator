from django.urls import path

from .views import ListMovie, DetailMovie, RandomMovieView

urlpatterns = [
    path('<int:pk>/', DetailMovie.as_view(), name='movie_detail'),
    path('', ListMovie.as_view(), name='movie_list'),
    path('get_random_movie/', RandomMovieView.as_view(), name='get_random_movie'),
]