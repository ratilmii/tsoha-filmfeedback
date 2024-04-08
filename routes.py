from app import app
from flask import session, render_template, request, redirect
import reviews, users, films

@app.route("/")
def index():
    username = None
    if users.user_id():
        # If the user is logged in, retrieve the username
        username = users.user_name()
    return render_template("index.html", username=username)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not username or not password:
            render_template("error.html", message="Please enter both username and password")
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Incorrect login information")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Make sure the password confirmation matches.")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Signup failed.¨")

@app.route("/browse")
def browse():
    list_of_films = films.get_list_chronological_ascending()
    if not list_of_films:
        return render_template("/error.html", message="No movies in database! What happened?")
    else:
        return render_template("browse.html", films=list_of_films)

@app.route("/films/<string:url_title>")
def film(url_title):
    movie = films.get_film_information(url_title)
    if not movie:
        return render_template("error.html", message="Movie not found")

    user_id = users.user_id()
    if user_id:
        user_review = reviews.get_user_review(user_id, movie['id'])
    else:
        user_review = None

    other_reviews = reviews.get_reviews_for_movie(user_id, movie['id'])

    return render_template("film.html", user_id=user_id, movie=movie, user_review=user_review, reviews=other_reviews)

@app.route("/submit_review", methods=["POST"])
def submit_review():
    if request.method == "POST":
        user_id = users.user_id()
        if not users.user_id():
            return redirect("login")

        movie_id = request.form["movie_id"]
        review_text = request.form["review_text"]
        star_rating = request.form["star_rating"]

        if star_rating is None:
            return "Please select a star rating"

        # Convert star_rating to float
        star_rating = round(float(star_rating), 1)

        # Call the function to add the review to the database
        reviews.add_review(movie_id, user_id, review_text, star_rating)

        # Redirect the user back to the film page
        url_title = films.get_url_title(movie_id)
        if url_title:
            return redirect(f"films/{url_title}")
        else:
            return render_template("error.html", message="Movie not found")
