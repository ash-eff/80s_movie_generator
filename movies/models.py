from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year =  models.CharField(max_length=4)
    rating = models.CharField(max_length=10)
    runtime = models.CharField(max_length=10)
    genre = models.CharField(max_length=255)
    description = models.TextField()
    director = models.CharField(max_length=255)
    stars = models.TextField()
    movie_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
