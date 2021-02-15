from django.shortcuts import render
from films.models import Film, ListName, FilmList, FilmLike, ListLike
from my_profile.models import Review, SeenFilm, ReviewLike
from django.db.models import Count
from django.views import View


class Homepage(View):
    def get(self, request):
        first_slide = Film.objects.all()[:4]
        second_slide = Film.objects.all()[4:8]
        reviews = Review.objects.all().order_by('-date')[:6]
        reviews_liked = []
        dictionary = FilmLike.objects.values("film_id").annotate(count=Count('film')).order_by("-count")[:6]
        popular_films = []
        for ele in dictionary:
            film = Film.objects.get(id=ele['film_id'])
            popular_films.append(film)
        liked_lists = ListLike.objects.values("list_id").annotate(count=Count('user')).order_by("-count")[:3]
        list_names = []
        for liked_list in liked_lists:
            list_names.append(ListName.objects.get(id=liked_list['list_id']))
        list_films = []
        for name in list_names:
            list_films.append(list(FilmList.objects.filter(list=name)[:3]))
        if request.user.is_authenticated:
            for r in reviews:
                liked = list(ReviewLike.objects.filter(review=r, user=request.user))
                reviews_liked.append((r, liked))
            return render(request, 'homepage/homepage.html',
                          {'first_slide': first_slide, 'second_slide': second_slide, 'reviews': reviews,
                           'popular_films': popular_films,
                           'list_films': list_films, 'list_names': list_names, 'reviews_liked': reviews_liked})
        else:
            return render(request, 'homepage/homepage.html',
                          {'first_slide': first_slide, 'second_slide': second_slide, 'reviews': reviews,
                           'popular_films': popular_films,
                           'list_films': list_films, 'list_names': list_names})
