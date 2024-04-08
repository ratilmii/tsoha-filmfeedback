from db import db
from sqlalchemy.sql import text

def get_list_chronological_ascending():
    movie_sql = """
    SELECT M.title, M.release_year, M.director, ROUND(AVG(R.star_rating), 2) AS avg_rating, REPLACE(REPLACE(LOWER(M.title), ' ', '-'), ':', '') AS url_title
    FROM Movies M
    LEFT JOIN Reviews R ON M.id = R.movie_id
    GROUP BY M.title, M.release_year, M.director
    ORDER BY M.release_year
    """
    result = db.session.execute(text(movie_sql))
    return result.fetchall()

def get_film_information(url_title):
    movie_sql = """
    SELECT M.id, M.title, M.release_year, M.director, M.runtime, M.plot_summary, ROUND(AVG(R.star_rating), 2) AS avg_rating, REPLACE(REPLACE(LOWER(M.title), ' ', '-'), ':', '') AS url_title
    FROM Movies M
    LEFT JOIN Reviews R ON M.id = R.movie_id
    WHERE REPLACE(REPLACE(LOWER(M.title), ' ', '-'), ':', '') = :url_title
    GROUP BY M.id
    """
    movie_result = db.session.execute(text(movie_sql), {'url_title': url_title})
    movie_data = movie_result.fetchone()

    if movie_data:
        keys_list = list(movie_result.keys())
        values_list = list(movie_data)
        movie_info = {keys_list[i]: values_list[i] for i in range(len(keys_list))}

        genres_sql = """
        SELECT G.genre_name
        FROM Genres G
        JOIN Movie_Genres MG ON G.id = MG.genre_id
        WHERE MG.movie_id = :movie_id
        """

        genres_result = db.session.execute(text(genres_sql), {'movie_id': movie_data[0]})
        genres = genres_result.fetchall()
        movie_info['genres'] = genres

        actors_sql = """
        SELECT A.actor_name
        FROM Actors A
        JOIN Movie_Actors MA ON A.id = MA.actor_id
        WHERE MA.movie_id = :movie_id
        """
        actors_result = db.session.execute(text(actors_sql), {'movie_id': movie_data[0]})
        actors = actors_result.fetchall()
        movie_info['actors'] = actors

        return movie_info

def get_url_title(movie_id):
    sql = "SELECT REPLACE(REPLACE(LOWER(title), ' ', '-'), ':', '') FROM Movies WHERE id = :movie_id"
    result = db.session.execute(text(sql), {'movie_id': movie_id})

    return result.fetchone()[0]
