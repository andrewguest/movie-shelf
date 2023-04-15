from typing import Union

from fastapi import APIRouter

from database.config import movies_collection


router = APIRouter(tags=["movies"])


@router.get("/movies")
async def get_all_movies(genre: Union[str, None] = None):
    """GET all movies without using the `genre` query parameter or GET all movies with the provided `genre` filter"""
    if genre:
        res = movies_collection.fetch({"genres?contains": genre})
    else:
        res = movies_collection.fetch()

    all_movies = res.items

    # continue to fetch results as long as `res.last` is True
    while res.last:
        res = movies_collection.fetch(last=res.last)
        all_movies += res.items

    return all_movies


@router.get("/movies/release_years")
async def list_all_release_years():
    """GET all distinct release years from the database to use for filtering"""

    res = movies_collection.fetch()
    all_movies = res.items

    while res.last:
        res = movies_collection.fetch(last=res.last)
        all_movies += res.items

    unique_release_years = []

    for movie in all_movies:
        if int(movie["release_year"]) not in unique_release_years:
            unique_release_years.append(int(movie["release_year"]))

    return sorted(unique_release_years)
