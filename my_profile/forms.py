from django import forms
from . import models
from films import models as film_models
from accounts import models as accounts_models


class AddFilm(forms.ModelForm):
    class Meta:
        model = models.Watch
        fields = ['film']


class AddReview(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['body', 'rating']


class EditReview(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['body', 'rating']


class CreateList(forms.ModelForm):
    class Meta:
        model = film_models.ListName
        fields = ['list_name', 'body']


class FilmToList(forms.ModelForm):
    class Meta:
        model = film_models.FilmList
        fields = ['film']


class ProfilePicture(forms.ModelForm):
    class Meta:
        model = accounts_models.Profile
        fields = ['picture']
