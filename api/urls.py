from django.urls import path
from ninja import NinjaAPI

from .movies.apis import movies_api


api = NinjaAPI()
api.add_router("movies/", movies_api)

urlpatterns = [
    path("api/", api.urls, name="api")
]
