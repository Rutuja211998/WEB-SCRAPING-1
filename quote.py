"""
This file containing pagination scraping for the website.
Author: Rutuja Tikhile.
Data:11/3/2020
"""
import requests
from bs4 import BeautifulSoup
import csv

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')

quotes = []  # a list to store quotes

table = soup.find('div', attrs={'id': 'container'})
# table = soup.find('div', {'class': 'container'})
print(table)

for row in table.findAll('div', attrs={'class': 'quote'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.h6.text
    quote['author'] = row.p.text
    quotes.append(quote)

filename = 'inspirational_quotes.csv'
with open(filename, 'wb') as f:
    w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)