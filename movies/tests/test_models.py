from ..models import Movie, MovieStatus
import pytest
from datetime import date


@pytest.mark.django_db
def test_movies_model():
    assert Movie.objects.count() == 0
    today = date.today()
    movie = Movie.objects.create(
        name="name",
        protagonists="protagonists",
        poster="poster",
        start_date=today,
        status=MovieStatus.COMINGUP,
        ranking=10
    )
    assert movie.name == "name"
    assert movie.protagonists == "protagonists"
    assert movie.poster == "poster"
    assert movie.start_date == today
    assert movie.status == MovieStatus.COMINGUP
    assert movie.ranking == 10
