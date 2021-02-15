from django.shortcuts import render, redirect
from .models import Film, Genre, FilmLike, ListLike
from my_profile.models import Review, SeenFilm, Watch, ReviewLike
from films.models import FilmList, ListName
from django.views import View
from django.views.generic import ListView
from my_profile import forms
from django.db.models import Count, Avg
from django.http import JsonResponse


class Movies(ListView):
    model = Film
    template_name = 'films/movies.html'
    context_object_name = 'films'
    paginate_by = 20


class Search(View):
    def post(self, request):
        keyword = request.POST.get("keyword")
        films = Film.objects.filter(title__icontains=keyword)
        reviews = Review.objects.filter(film__title__icontains=keyword)
        film_list_objects = FilmList.objects.filter(film__title__icontains=keyword)
        list_names = []
        for film_list in film_list_objects:
            list_names.append(ListName.objects.get(id=film_list.list_id))
        list_films = []
        for name in list_names:
            list_films.append((name, list(FilmList.objects.filter(list=name)[:3])))
        return render(request, 'films/search.html', {'films': films, 'reviews': reviews, 'list_films': list_films})


# def movies(request):
#     keyword = request.GET.get("results")
#     if keyword:
#         films = Film.objects.filter(title__icontains=keyword)
#         return render(request, 'films/movies.html', {'films': films})
#     films = Film.objects.all().order_by('title')
#     return render(request, 'films/movies.html', {'films': films})


class FilmDetail(View):
    def get(self, request, id):
        detailed_film = Film.objects.get(id=id)
        genres = detailed_film.genres.all()
        avg_rating = Review.objects.filter(film=detailed_film).aggregate(avg=Avg('rating'))['avg']
        rating_num = 0
        if Review.objects.filter(film=detailed_film).values('film_id').annotate(rating_num=Count('rating')):
            rating_num = \
                Review.objects.filter(film=detailed_film).values('film_id').annotate(rating_num=Count('rating'))[0][
                    'rating_num']

        film_reviews = Review.objects.filter(film__title=detailed_film.title)
        author_num = Review.objects.filter(film=detailed_film).values('author_id').annotate(
            review_num=Count('author_id'))
        author_num = len(author_num)
        reviews_with_likes = []
        if request.user.is_authenticated:
            form = forms.AddReview()
            added_watchlist = list(Watch.objects.filter(user=request.user, film=detailed_film))
            reviewed = list(Review.objects.filter(author=request.user, film=detailed_film))
            if reviewed:
                review = reviewed[0]
            else:
                review = []
            if film_reviews:
                for r in film_reviews:
                    liked = list(ReviewLike.objects.filter(review=r, user=request.user))
                    reviews_with_likes.append((r, liked))
            like_number = len(FilmLike.objects.filter(film_id=id))
            liked = list(FilmLike.objects.filter(film=detailed_film, user=request.user))
            added = list(SeenFilm.objects.filter(film=detailed_film, user=request.user))
            return render(request, 'films/film_detail.html',
                          {'detailed_film': detailed_film, 'genres': genres, 'film_reviews': film_reviews,
                           'added': added, 'reviewed': reviewed, 'review': review,
                           'liked': liked, 'added_watchlist': added_watchlist, 'form': form,
                           'reviews_with_likes': reviews_with_likes, 'like_number': like_number,
                           'avg_rating': str(avg_rating)[:3], 'rating_num': rating_num, 'author_num': author_num})

        else:
            return render(request, 'films/film_detail.html',
                          {'detailed_film': detailed_film, 'genres': genres, 'film_reviews': film_reviews})


# def film_detail(request, id):
#     detailed_film = Film.objects.get(id=id)
#     genres = detailed_film.genres.all()
#     film_reviews = Review.objects.filter(film__title=detailed_film.title)
#     if request.user.is_authenticated:
#         added_watchlist = list(Watch.objects.filter(user=request.user, film=detailed_film))
#         reviewed = list(Review.objects.filter(author=request.user, film=detailed_film))
#         if reviewed:
#             review = reviewed[0]
#         else:
#             review = []
#         liked = list(FilmLike.objects.filter(film=detailed_film, user=request.user))
#         added = list(SeenFilm.objects.filter(film=detailed_film, user=request.user))
#         return render(request, 'films/film_detail.html',
#                       {'detailed_film': detailed_film, 'genres': genres, 'film_reviews': film_reviews,
#                        'added': added, 'reviewed': reviewed, 'review': review,
#                        'liked': liked, 'added_watchlist': added_watchlist})
#
#     else:
#         return render(request, 'films/film_detail.html',
#                       {'detailed_film': detailed_film, 'genres': genres, 'film_reviews': film_reviews})
class Genres(View):
    def get(self, request):
        all_genres = Genre.objects.all().order_by('name')
        return render(request, 'films/genres.html', {'genres': all_genres})


# def genres(request):
#     keyword = request.GET.get("keyword")
#     if keyword:
#         all_genres = Genre.objects.filter(name__icontains=keyword)
#         return render(request, 'films/genres.html', {'genres': all_genres})
#     all_genres = Genre.objects.all().order_by('name')
#     return render(request, 'films/genres.html', {'genres': all_genres})


class GenreDetail(View):
    def get(self, request, id):
        genre = Genre.objects.get(id=id)
        genre_films = Film.objects.filter(genres__name=genre.name)
        return render(request, 'films/genre_detail.html', {'genre_films': genre_films, 'genre': genre})


# def genre_detail(request, id):
#     genre = Genre.objects.get(id=id)
#     genre_films = Film.objects.filter(genres__name=genre.name)
#     return render(request, 'films/genre_detail.html', {'genre_films': genre_films, 'genre': genre})


class WatchedFilms(View):
    def get(self, request):
        seen_films = SeenFilm.objects.filter(user=request.user)
        return render(request, 'films/watched_films.html', {'seen_films': seen_films})


# def watched_films(request):
#     seen_films = SeenFilm.objects.filter(user=request.user)
#     return render(request, 'films/watched_films.html', {'seen_films': seen_films})

class AllLists(View):
    def get(self, request):
        list_names = ListName.objects.all().order_by('-date')
        list_films = []
        if request.user.is_authenticated:
            for name in list_names:
                if list(FilmList.objects.filter(list=name)):
                    last_added = FilmList.objects.filter(list=name).order_by('-date')[0]
                    list_films.append((list(FilmList.objects.filter(list=name)[:3]), name, last_added.date,
                                       list(ListLike.objects.filter(list=name, user=request.user))))
        else:
            for name in list_names:
                if list(FilmList.objects.filter(list=name)):
                    last_added = FilmList.objects.filter(list=name).order_by('-date')[0]
                    list_films.append((list(FilmList.objects.filter(list=name)[:3]), name, last_added.date))
        return render(request, 'films/all_lists.html', {'list_films': list_films})

# def all_lists(request):
#     list_names = ListName.objects.all().order_by('-date')
#     list_films = []
#     for name in list_names:
#         if list(FilmList.objects.filter(list=name)):
#             last_added = FilmList.objects.filter(list=name).order_by('-date')[0]
#             list_films.append((list(FilmList.objects.filter(list=name)[:3]), name, last_added.date))
#     return render(request, 'films/all_lists.html', {'list_films': list_films})
