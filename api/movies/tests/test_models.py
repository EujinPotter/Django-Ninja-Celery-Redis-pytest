from api.movies.models import Movie, MovieStatus
import pytest
from datetime import datetime


@pytest.mark.django_db
def test_movies_model():
    assert Movie.objects.count() == 0
    start_time = datetime.now()
    movie = Movie.objects.create(
        name="name",
        protagonists="protagonists",
        poster="poster",
        start_time=start_time,
        status=MovieStatus.COMINGUP,
        ranking=10
    )
    assert movie.name == "name"
    assert movie.protagonists == "protagonists"
    assert movie.poster == "poster"
    assert movie.start_time == start_time
    assert movie.status == MovieStatus.COMINGUP
    assert movie.ranking == 10
