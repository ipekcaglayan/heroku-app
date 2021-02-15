# import os
# os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoProject3.settings'
# import django
# django.setup()
from films.models import Genre, Film
from my_profile.models import Review, Watch
import csv
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'populate'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        Film.objects.all().delete()
        Genre.objects.all().delete()
        Review.objects.all().delete()
        Watch.objects.all().delete()
        with open('deneme2.tsv', newline='') as csvfile:
            file = csv.reader(csvfile, delimiter='\t')
            genre_objects = Genre.objects.all()
            dict = {}
            for genre_object in genre_objects:
                dict[genre_object.name] = genre_object
            for row in file:
                if row[0] != 'tconst':
                    movie = Film(tconst=row[0], title=row[2], year=row[5], minutes=row[7])
                    movie.save()
                    titles = row[8].split(',')
                    for genre_name in titles:
                        if genre_name in dict.keys():
                            genre = dict[genre_name]
                            movie.genres.add(genre)
                        else:
                            new_genre = Genre(name=genre_name)
                            new_genre.save()
                            dict[genre_name] = new_genre
                            movie.genres.add(new_genre)
