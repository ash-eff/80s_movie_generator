from django.core.management.base import BaseCommand
from movies.models import Movie
import json

class Command(BaseCommand):
    help = 'Import movie data from a JSON file'
    json_file_path = 'movie_data.json'

    def handle(self, *args, **options):
        try:
            with open(self.json_file_path, 'r') as json_file:
                movie_data = json.load(json_file)

                for data in movie_data:
                    Movie.objects.create(
                        title=data['Title'],
                        release_year=data['Release Year'],
                        rating=data['Rating'],
                        runtime=data['Runtime'],
                        description=data['Description'],
                        director=data['Director'],
                        genre=data['Genre'],
                        stars=data['Stars'],
                        movie_url=data['MovieURL'],
                    )
                
                self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {json_file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format in the file.'))
          
