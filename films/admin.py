from django.contrib import admin
from .models import Film, ListName, FilmList, Genre, FilmLike, ListLike

admin.site.register(Film)
admin.site.register(ListName)
admin.site.register(FilmList)
admin.site.register(Genre)
admin.site.register(FilmLike)
admin.site.register(ListLike)
