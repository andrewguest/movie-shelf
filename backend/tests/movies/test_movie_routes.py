from unittest import mock
from fastapi.testclient import TestClient

from app.main import app
from tests.data import mock_movie_data


client = TestClient(app)


# `patch` any calls to the movies_collection.fetch() function
#   within routes/movie_router with a mock response
@mock.patch("routes.movie_router.movies_collection.fetch")
def test_get_all_movies(mock_deta_fetch):
    """GET the `/movies` route"""

    # mock response where `last=False`
    mock_deta_fetch.return_value = mock.Mock(
        items=mock_movie_data.list_of_movies, last=False
    )

    response = client.get("/movies")

    assert response.status_code == 200
    assert len(response.json()) == len(mock_movie_data.list_of_movies)


@mock.patch("routes.movie_router.movies_collection.fetch")
def test_list_all_release_years(mock_deta_fetch):
    """GET the `/movies/release_years` route"""

    unique_release_years = [
        int(movie["release_year"]) for movie in mock_movie_data.list_of_movies
    ]
    unique_release_years.sort()
    unique_release_years = list(set(unique_release_years))

    # mock the Deta response
    mock_deta_fetch.return_value = mock.Mock(
        items=mock_movie_data.list_of_movies, last=False
    )

    response = client.get("/movies/release_years")

    assert response.status_code == 200
    assert response.json() == unique_release_years
