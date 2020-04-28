"""
This file containing testing using selenium chrome driver.
Author: Rutuja Tikhile.
Data:21/4/2020
"""
from selenium import webdriver


chromedriver="C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("https:google.com")

url = driver.current_url
print(url)
print(driver.title)
driver.close()