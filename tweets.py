"""
This file containing twitter data scraping form the twiiter account.
Author: Rutuja Tikhile.
Data:5/4/2020
"""
import requests
from bs4 import BeautifulSoup
from query.db_query import Query
db_obj = Query()

url = 'https://twitter.com/TheOnion'
data = requests.get(url)
# html = BeautifulSoup(data.text, 'html.parser')
# print(html)
all_tweets = []
html = BeautifulSoup(data.text, 'html.parser')
timeline = html.select('#timeline li.stream-item')
for tweet in timeline:
    tweet_id = tweet['data-item-id']
    tweet_text = tweet.select('p.tweet-text')[0].get_text()
    all_tweets.append((tweet_id,tweet_text))
    # print(all_tweets)
    db_obj.insert_many(table_name="scrape", data=all_tweets)