"""
This file containing pagination scraping for the website.
Author: Rutuja Tikhile.
Data:10/4/2020
"""
from bs4 import BeautifulSoup
import requests

pages = [10, 20, 30, 40, 50]

for page in pages:
    source = requests.get('https://www.indeed.com/jobs?q=data+scientist&start={}'.format(page)).text

    soup = BeautifulSoup(source, 'html.parser')

    for jobs in soup.find_all(class_='result'):

        try:
            title = jobs.h2.text.strip()
        except Exception as e:
            title = None
        print('Job title:', title)

        try:
            company = jobs.span.text.strip()
        except Exception as e:
            company = None
        print('Company:', company)

        try:
            location = jobs.find('span', class_='location').text.strip()
        except Exception as e:
            location = None
        print('Location:', location)

        try:
            summary = jobs.find('span', class_='summary').text.strip()
        except Exception as e:
            summary = None
        print('Summary:', summary)

        try:
            salary = jobs.find('span', class_='no-wrap').text.strip()
        except Exception as e:
            salary = None
        print('Salary:', salary)

        print('------------------')