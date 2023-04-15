from django.urls import path
from .views import MovieListAPIView, MovieTrendingListAPIView

urlpatterns = [
  path("", MovieListAPIView.as_view(), name="movie-list"),
  path("trending", MovieTrendingListAPIView.as_view(), name="movie-trending-list")
]
