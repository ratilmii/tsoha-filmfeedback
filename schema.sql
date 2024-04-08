-- Users table
CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    is_admin BOOLEAN
);

-- Movies table
CREATE TABLE Movies (
    id SERIAL PRIMARY KEY,
    title TEXT,
    runtime INTEGER,
    director TEXT,
    release_year INTEGER,
    plot_summary TEXT
);

-- Genres table
CREATE TABLE Genres (
    id SERIAL PRIMARY KEY,
    genre_name TEXT
);

-- Movie_Genres table
CREATE TABLE Movie_Genres (
    movie_id INTEGER REFERENCES Movies(id),
    genre_id INTEGER REFERENCES Genres(id),
    PRIMARY KEY (movie_id, genre_id)
);

-- Actors table
CREATE TABLE Actors (
    id SERIAL PRIMARY KEY,
    actor_name TEXT
);

-- Movie_Actors table
CREATE TABLE Movie_Actors (
    movie_id INTEGER REFERENCES Movies(id),
    actor_id INTEGER REFERENCES Actors(id),
    PRIMARY KEY (movie_id, actor_id)
);

-- Reviews table
CREATE TABLE Reviews (
    id SERIAL PRIMARY KEY,
    movie_id INTEGER REFERENCES Movies(id),
    user_id INTEGER REFERENCES Users(id),
    review_text TEXT,
    star_rating DECIMAL(2,1),
    time_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Likes_Dislikes table
CREATE TABLE Likes_Dislikes (
    id SERIAL PRIMARY KEY,
    review_id INTEGER REFERENCES Reviews(id),
    user_id INTEGER REFERENCES Users(id),
    reaction INTEGER
);


-- Creating the initial database with ten famous movies
-- Insert movies
INSERT INTO Movies (title, runtime, director, release_year, plot_summary) 
VALUES 
    ('The Godfather', 175, 'Francis Ford Coppola', 1972, 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'),
    ('Star Wars: Episode IV - A New Hope', 121, 'George Lucas', 1977, 'Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee, and two droids to save the galaxy from the Empire''s world-destroying battle station.'),
    ('Titanic', 194, 'James Cameron', 1997, 'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.'),
    ('The Shawshank Redemption', 142, 'Frank Darabont', 1994, 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'),
    ('The Lord of the Rings: The Fellowship of the Ring', 179, 'Peter Jackson', 2001, 'A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.'),
    ('Forrest Gump', 142, 'Robert Zemeckis', 1994, 'The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate, and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.'),
    ('The Dark Knight', 152, 'Christopher Nolan', 2008, 'When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham. The Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.'),
    ('Pulp Fiction', 154, 'Quentin Tarantino', 1994, 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'),
    ('Jurassic Park', 127, 'Steven Spielberg', 1993, 'During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok.'),
    ('Inception', 148, 'Christopher Nolan', 2010, 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.')
;

-- Insert genres
INSERT INTO Genres (genre_name) 
VALUES 
    ('Crime'),
    ('Sci-Fi'),
    ('Romance'),
    ('Drama'),
    ('Fantasy'),
    ('Comedy'),
    ('Action'),
    ('Thriller'),
    ('Adventure')
;

-- Insert movie-genre relationships
INSERT INTO Movie_Genres (movie_id, genre_id)
VALUES
    (1, 1), (1, 4),  -- The Godfather - Crime, Drama
    (2, 2), (2, 9), (2, 7), -- Star Wars - Sci-Fi, Adventure, Action
    (3, 3), (3, 4), -- Titanic - Romance, Drama
    (4, 4), (4, 1), -- Shawshank Redemption - Drama, Crime
    (5, 5), (5, 9), (5, 7), -- Lord of the Rings - Fantasy, Adventure, Action
    (6, 4), (6, 6), (6, 3), -- Forrest Gump - Drama, Comedy, Romance
    (7, 7), (7, 4), (7, 8), (7, 1), -- The Dark Knight - Action, Drama, Thriller, Crime
    (8, 1), (8, 8), -- Pulp Fiction - Crime, Thriller
    (9, 2), (9, 9), -- Jurassic Park - Sci-Fi, Adventure
    (10, 2), (10, 7), (10, 9)  -- Inception - Sci-Fi, Action, Adventure
;

-- Insert actors
INSERT INTO Actors (actor_name)
VALUES
    ('Marlon Brando'),
    ('Al Pacino'),
    ('James Caan'),
    ('Robert Duvall'),
    ('Mark Hamill'),
    ('Harrison Ford'),
    ('Carrie Fisher'),
    ('Kate Winslet'),
    ('Leonardo DiCaprio'),
    ('Tom Hanks'),
    ('Christian Bale'),
    ('Heath Ledger'),
    ('John Travolta'),
    ('Uma Thurman'),
    ('Samuel L. Jackson'),
    ('Joseph Gordon-Levitt'),
    ('Ken Watanabe'),
    ('Sam Neill'),
    ('Laura Dern'),
    ('Jeff Goldblum'),
    ('Michael Caine'),
    ('Elijah Wood'),
    ('Ian McKellen'),
    ('Viggo Mortensen'),
    ('Sean Bean'),
    ('Sean Astin'),
    ('Tim Robbins'),
    ('Morgan Freeman'),
    ('Bob Gunton'),
    ('Peter Cushing'),
    ('Alec Guinness')
;

-- Insert movie-actor relationships
INSERT INTO Movie_Actors (movie_id, actor_id)
VALUES
    (1, 1), (1, 2), (1, 3), (1, 4), -- The Godfather
    (2, 5), (2, 6), (2, 7), (2, 30), (2, 31), -- Star Wars
    (3, 8), (3, 9), -- Titanic
    (4, 27), (4, 28), (4, 29), -- Shawshank Redemption
    (5, 22), (5, 23), (5, 24), (5, 25), (5, 26), -- Lord of the Rings
    (6, 10), -- Forrest Gump
    (7, 11), (7, 12), (7, 21), -- The Dark Knight
    (8, 13), (8, 14), (8, 15), -- Pulp Fiction
    (9, 18), (9, 19), (9, 20), -- Jurassic Park
    (10, 9), (10, 16), (10, 17) -- Inception
;
