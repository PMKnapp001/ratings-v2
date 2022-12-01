"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!

@app.route('/')
def homepage():

    return render_template('homepage.html')


@app.route('/movies')
def all_movies():

    movies = crud.get_all_movies()

    return render_template('movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):

    movie= crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)


@app.route('/users')
def all_users():

    users = crud.get_all_users()

    return render_template('users.html', users=users )


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")


@app.route("/login", methods=["POST"])
def login_user():
    """Login user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        if user.password == password:
            session['user_id'] = user.user_id
            print(f"{user.email}'s test: user _ id = {session['user_id']}")
            flash("Logged In!")
        else:
            flash("Incorrect password...")
    else:
        flash("No account associated with email.")

    return redirect("/")


@app.route('/ratings/<movie_id>')
def rate_movie(movie_id):
    
    movie = movie_id

    if session.get('user_id'):
        score = request.args.get('rating')
        user = session['user_id']

        rating = crud.create_rating(score, movie, user)
        db.session.add(rating)
        db.session.commit()

        return redirect(f'/movies/{movie}')

    else:
        flash("You are not logged in!!!")
        return redirect(f'/movies/{movie}')


@app.route('/users/<user_id>')
def show_user(user_id):

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)

    


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)


