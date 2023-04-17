from django.urls import path
from .apis import movies_api

urlpatterns = [
    path("/", movies_api.urls, name="movie-list"),
]
