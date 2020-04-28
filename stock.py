"""
This file containing scraping form the stock website for the stock feeds.
Author: Rutuja Tikhile.
Data:10/4/2020
"""
import requests
from bs4 import BeautifulSoup


def parsePrice():
    url = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
    soup = BeautifulSoup(url.text, "html.parser")
    price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    # print(price)
    return price


while True:
    print('the current price:'+ str(parsePrice()))