from db import db
from sqlalchemy.sql import text

def add_review(movie_id, user_id, review_text, star_rating):

    sql = """
    INSERT INTO Reviews (movie_id, user_id, review_text, star_rating, time_posted)
    VALUES (:movie_id, :user_id, :review_text, :star_rating, CURRENT_TIMESTAMP)
    """
    db.session.execute(text(sql), {'movie_id': movie_id, 'user_id': user_id, 'review_text': review_text, 'star_rating': star_rating})
    db.session.commit()

def get_user_review(user_id, movie_id):
    sql = "SELECT * FROM Reviews WHERE user_id = :user_id AND movie_id = :movie_id"
    result = db.session.execute(text(sql), {'user_id': user_id, 'movie_id': movie_id})
    return result.fetchone()

def get_reviews_for_movie(user_id, movie_id):
    sql = """
    SELECT R.id, R.user_id, R.review_text, R.star_rating, U.username
    FROM Reviews R
    JOIN Users U ON R.user_id = U.id
    WHERE R.movie_id = :movie_id
    AND R.user_id != :user_id
    """
    result = db.session.execute(text(sql), {'movie_id': movie_id, 'user_id': user_id})
    reviews = []
    for row in result.fetchall():
        review = {
            'id': row[0],
            'user_id': row[1],
            'review_text': row[2],
            'star_rating': row[3],
            'username': row[4]
        }
        reviews.append(review)
    return reviews
