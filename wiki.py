"""
This file containing scarping for the wikipedia using beautiful soup.
Author: Rutuja Tikhile.
Data:18/4/2020
"""
import bs4
import requests

response = requests.get("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=%27")
movieNames = []  # Movie Names
years = []  # Release Years
genres = []  # Movie Genres
imdbRatings = []  # IMDB Ratings

if response is not None:
    page = bs4.BeautifulSoup(response.text, 'html.parser')
    movieContainers = page.find_all('div', class_ = 'lister-item mode-advanced')

    for container in movieContainers:

        # Movie Name
        name = container.h3.a.text
        movieNames.append(name)

        # Release Year
        year = container.h3.find('span', class_ = 'lister-item-year').text
        years.append(int(year[-5:-1]))

        # Movie Genre
        genre = container.p.find('span', class_ = 'genre') \
            .text.strip('\n').strip()
        genres.append(genre.split(', '))

        # IMDB Rating
        rating = container.strong.text
        imdbRatings.append(float(rating))

print(movieNames, years, genres, imdbRatings)
