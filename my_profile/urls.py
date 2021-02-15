from django.urls import path
from . import views
from films import views as films_views

app_name = 'profile'
urlpatterns = [
    path('profile/<str:username>/<str:city>/', views.MyProfile.as_view(), name='profile'),
    path('review_detail/<int:id>/', views.ReviewDetail.as_view(), name="detail"),
    # path('watchlater/', views.watch_later, name='watch later'),
    path('addreview/<int:id>/', views.AddReview.as_view(), name='add review'),
    path('edit/<int:id>/', views.EditReview.as_view(), name='edit review'),
    path('ajax/', views.WatchedButtonAjax.as_view(), name='buttonAjax'),
    path('like/', views.LikeButtonAjax.as_view(), name='likeAjax'),
    path('watchl/', views.WatchlistAjax.as_view(), name='watchlist ajax'),
    path('later/', views.WatchLaterAjax.as_view(), name='watchLaterAjax'),
    path('filmlistajax/', views.RemoveListAjax.as_view(), name='film_list_ajax'),
    path('deletelist/', views.DeleteListAjax.as_view(), name='delete_list_ajax'),
    path('watchedfilms/', films_views.WatchedFilms.as_view(), name='watched films'),
    path('list_detail/<int:id>/', views.ListDetail.as_view(), name='list detail'),
    path('createlist/', views.CreateList.as_view(), name='create list'),
    path('addfilm/<int:id>/', views.FilmToList.as_view(), name='film to list'),
    path('watchedajax/', views.WatchedAjax.as_view(), name='watchedAjax'),
    path('deletereviewajax/', views.DeleteReviewAjax.as_view(), name='delete review ajax'),
    path('likereview/', views.LikeReview.as_view(), name='like review ajax'),
    path('likelist/', views.LikeList.as_view(), name='like list ajax'),
    path('upload_picture/', views.UploadPicture.as_view(), name='upload picture'),
    path('recommended/<int:id>/', views.RecommendMovie.as_view(), name='recommend'),
    path('deneme/', views.Deneme.as_view(), name='deneme'),
    path('content-based-recommender/<int:id>/', views.ContentBasedRecommender.as_view(),
         name='content_based_recommender'),

]
