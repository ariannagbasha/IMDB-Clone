import sqlite3
import requests

# url = "https://imdb-api.com/en/API/Top250Movies/{SECRET_KEY}"
# REGISTER FOR KEY at:
# https://imdb-api.com/
url = ""

if url == "":
    print('Please add api key to url var in main.py')
else:
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    table_name = 'imdb_app_movie'

    def add_250_movies(table_name, movies):
        query = f'INSERT INTO {table_name}(title, rating, counting, crew, image) VALUES (:title, :imDbRating, :imDbRatingCount, :crew, :image)'
        c.executemany(query, movies)
        conn.commit()

    response = requests.request("GET", url)
    response_data = response.json()

    add_250_movies(table_name, response_data['items'])
    c.close()