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


def get_all_movies():
    """"Gets list of all movies"""
    
    all_movies = db.session.query(Movie.movie_id, Movie.title).all()

    return all_movies


def get_movie_by_id(movie_id):
    """"Gets a movie by its id"""

    movie = Movie.query.get(movie_id)

    return movie


def get_all_users():
    """"Gets list of all users"""

    return User.query.all()


def get_user_by_id(user_id):
    """"Gets a user by their id"""

    user = User.query.get(user_id)

    return user


def get_user_by_email(email):
    """Gets a user by their email"""

    email = User.query.filter(User.email== email).first()

    if email:
        return email
    
    else:
        return None


def create_rating(score, movie_id, user_id):

    rating = Rating(score=score, movie_id=movie_id, user_id=user_id)

    return rating



if __name__ == '__main__':
    from server import app
    connect_to_db(app)