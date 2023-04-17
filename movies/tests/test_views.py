from django.test import Client
import pytest

import json


@pytest.mark.django_db(transaction=True)
def test_api_moves():
    client = Client()
    # Issue a GET request to the URL you want to test
    response = client.get("/api/movies", follow=True)
    assert response.status_code == 200

    content = json.loads(response.content)
    assert type(content) == list


@pytest.mark.django_db(transaction=True, databases=["default", "sync_mongo"])
def test_api_moves_trending():
    client = Client()
    # Issue a GET request to the URL you want to test
    response = client.get("/api/movies/trending", follow=True)

    assert response.status_code == 200

    content = json.loads(response.content)
    assert type(content) == list
