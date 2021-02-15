import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'filmdiary.settings'
import django
django.setup()
from films.models import Genre, Film
import csv

with open('deneme.tsv', newline='') as csvfile:
    s = csv.reader(csvfile, delimiter='\t')
    for row in s:
        if row[0] != 'tconst':
            g = Genre(name=row[8])
            g.save()
            m = Film(tconst=row[0], title=row[2], year=row[5], minutes=row[7], genre=g)
            m.save()
