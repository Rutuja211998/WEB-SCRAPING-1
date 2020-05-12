"""
Scraping instagram profile with beautiful soup.
Author : Rutuja Tikhile.
Date : 12/5/2020
"""
import requests
from bs4 import BeautifulSoup
import json


instagram_url = 'https://www.instagram.com'
profile_url = 'thesassthing_'
response = requests.get(f"{instagram_url}/{profile_url}")
print(response.status_code)
if response.ok:
    html = response.text
    bs_html = BeautifulSoup(html)
    # print(bs_html)
    scripts = bs_html.select('script[type="application/ld+json"]')
    script_content = json.loads(scripts[0].text.strip())
    print(json.dumps(script_content, indent=4, sort_keys=True))
    # main_entity_of_page = script_content['mainEntityofPage']
    # interaction_statistic = main_entity_of_page['interactionStatistic']
    # follower_count = interaction_statistic['userInteractionCount']
    # print(follower_count)