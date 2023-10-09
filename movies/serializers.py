from rest_framework import serializers

from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'release_year',
            'rating',
            'runtime',
            'genre',
            'description',
            'director',
            'stars',
            'movie_url',
        )
        model = Movie