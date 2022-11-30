"""CRUD Operations"""

from model import db, User, Movie, Rating, connect_to_db
from datetime import datetime


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def create_movie(user_title, user_overview, user_release_date, user_poster_path):
    """Create and return a new movie."""

    movie = Movie(
        title=user_title,
        overview=user_overview,
        release_date=user_release_date,
        poster_path=user_poster_path,
    )

    return movie

def create_rating(score, movie_id, user_id):

    rating = Rating(score=score, movie_id=movie_id, user_id=user_id)

    return rating



if __name__ == '__main__':
    from server import app
    connect_to_db(app)