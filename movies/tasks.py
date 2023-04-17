from django.db import models
from celery import shared_task
from .models import Movie, MovieStatus


@shared_task
def update_movie_ranking():
    # Get all movies with status="coming-up"
    coming_up_movies = Movie.objects.filter(status=MovieStatus.COMINGUP)
    coming_up_movies.update(ranking=models.F("ranking") + 10)
