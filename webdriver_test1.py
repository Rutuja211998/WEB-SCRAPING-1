"""
This file containing testing using selenium chrome driver.
Author: Rutuja Tikhile.
Data:21/4/2020
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driverpath = "C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(driverpath)
driver.get("https://www.google.com/")
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("computer")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()