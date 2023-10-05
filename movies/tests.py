from django.test import TestCase

from .models import Movie

class MovieModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.movie = Movie.objects.create(
            title='movie title',
            release_year='1982',
            rating='PG-13',
            runtime='109',
            genre='action',
            description="a really cool movie",
            director='director name',
            stars='some stars'
        )

    def test_model_content(self):
        self.assertEqual(self.movie.title,'movie title')
        self.assertEqual(self.movie.release_year,'1982')
        self.assertEqual(self.movie.rating,'PG-13')
        self.assertEqual(self.movie.runtime,'109')
        self.assertEqual(self.movie.genre,'action')
        self.assertEqual(self.movie.description,'a really cool movie')
        self.assertEqual(self.movie.director,'director name')
        self.assertEqual(self.movie.stars,'some stars')
        self.assertEqual(str(self.movie), 'movie title')

