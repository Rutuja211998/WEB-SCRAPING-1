"""
This file containing news data scraping form the indiatoday website.
Author: Rutuja Tikhile.
Data:1/4/2020
"""
import bs4
import requests

url = "https://www.indiatoday.in/india?page=4"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')

# last_links = soup.find(class_='story-section')
# print(last_links)
# print(soup.prettify())
for para in soup.find_all('p'):
    print(para.text)
# for links in soup.find_all('a'):  # To find all the links
#     link = links.get('href')
#     print(link)
# rows = soup.find_all('tr')
# for row in rows:          # Print all occurrences
#     print(row.get_text())