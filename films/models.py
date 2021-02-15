from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Film(models.Model):
    tconst = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    minutes = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    poster = models.ImageField(default='default.png', blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ListName(models.Model):
    list_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.list_name


class FilmList(models.Model):
    list = models.ForeignKey(ListName, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('list', 'film',)

    def __str__(self):
        return self.film.title


class FilmLike(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.film.title


class ListLike(models.Model):
    list = models.ForeignKey(ListName, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.list.list_name
