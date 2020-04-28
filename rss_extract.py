"""
This file containing scarping for the news website using beautiful soup and giving the lastest feed using rssfeed.
Author: Rutuja Tikhile.
Data:18/4/2020
"""
import requests
from bs4 import BeautifulSoup
from query.db_query import Query
db_obj = Query()


url = 'https://www.hindustantimes.com/rss/topnews/rssfeed.xml'
response = requests.get(url)
soup = BeautifulSoup(response.content, features="xml")
print(soup.prettify())
items = soup.find_all('item')
# print(items)
# print(len(items))
item = items[0]
# print(item)
print(item.title.text)
print(item.content['url'])
news_items = []
for item in items:
    news_item = {}
    news_item['title'] = item.title.text
    news_item['description'] = item.description.text
    news_item['link'] = item.link.text
    news_item['image'] = item.content['url']
    news_items.append(news_item)
print(news_items)








# db_obj.insert_many(data=news_items, table_name="rss")



