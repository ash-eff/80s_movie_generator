from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
import random

from .models import Movie
from.serializers import MovieSerializer

class ListMovie(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class DetailMovie(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class RandomMovieView(APIView):
    def get(self, request, format=None):
        item_count = Movie.objects.count()
        random_index = random.randint(0, item_count - 1)
        random_movie = Movie.objects.all()[random_index]
        serializer = MovieSerializer(random_movie)

        return Response(serializer.data)