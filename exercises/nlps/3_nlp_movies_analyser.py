# Algorithm to find movies based on genre

import nltk
from urllib.request import urlopen
from bs4 import BeautifulSoup
from googletrans import Translator

# URL with the list of movies and genres
url = "https://www.imdb.com/search/keyword/?keywords=genetics%2Cscientist&sort=moviemeter,asc&mode=detail&page=1&ref_=kw_ref_key"

# Load stopwords in Portuguese
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

# Get the HTML of the page
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Extract movie titles and genres from the HTML
movies_html = soup.find_all('h3', class_='lister-item-header')
genres_html = soup.find_all('span', class_='genre')

# Filter and clean the text
movies = [movie.find('a').text.lower() for movie in movies_html]
genres = [genre.text.strip().lower() for genre in genres_html]

# Map movies to genres
movie_genres = dict(zip(movies, genres))

# Create the translator
translator = Translator()

# Continuous loop
while True:
    # Prompt user for the desired genre
    desired_genre_pt = input("Digite o gênero desejado (ou 'chega' para sair): ").lower()

    if desired_genre_pt == "chega":
        print("Adeus...")
        break

    # Translate the genre to English
    desired_genre_en = translator.translate(desired_genre_pt, src='pt', dest='en').text.lower()

    # Filter movies related to the genre
    related_movies = [movie for movie, genre in movie_genres.items() if desired_genre_en in genre]

    # Print the related movies found
    if related_movies:
        print(f"Filmes relacionados ao genêro '{desired_genre_pt}':")
        for movie in related_movies:
            print(movie)
    else:
        print(f"Nenhum filme relacionado ao genêro '{desired_genre_pt}' foi encontrado.")
