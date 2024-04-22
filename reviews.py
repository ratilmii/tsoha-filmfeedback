from db import db
from sqlalchemy.sql import text

def add_review(movie_id, user_id, review_text, star_rating):
    sql = """
    INSERT INTO Reviews (movie_id, user_id, review_text, star_rating, time_posted)
    VALUES (:movie_id, :user_id, :review_text, :star_rating, CURRENT_TIMESTAMP)
    """
    db.session.execute(text(sql), {'movie_id': movie_id, 'user_id': user_id, 'review_text': review_text, 'star_rating': star_rating})
    db.session.commit()

def delete_review(review_id):
    sql = "DELETE FROM Reviews WHERE id = :review_id"
    db.session.execute(text(sql), {'review_id': review_id})
    db.session.commit()


def get_user_review(user_id, movie_id):
    sql = "SELECT * FROM Reviews WHERE user_id = :user_id AND movie_id = :movie_id"
    result = db.session.execute(text(sql), {'user_id': user_id, 'movie_id': movie_id})
    return result.fetchone()

def get_reviews_for_movie(user_id, movie_id):
    sql = """
    SELECT R.id, R.user_id, R.review_text, R.star_rating, R.likes, R.dislikes, U.username
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
            'likes': row[4],
            'dislikes': row[5],
            'username': row[6]
        }
        reviews.append(review)
    return reviews

def get_review_by_id(review_id):
    sql = "SELECT * FROM Reviews WHERE id = :review_id"
    result = db.session.execute(text(sql), {'review_id': review_id})
    return result.fetchone()

def get_movie_id_by_review(review_id):
    sql =  "SELECT movie_id FROM Reviews WHERE id = :review_id"
    result = db.session.execute(text(sql), {'review_id': review_id})
    return result.fetchone()[0]
