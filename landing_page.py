#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://beta.hesttia.com")

elem = driver.find_element_by_name("search_location")
elem.clear();
elem.send_keys("alcala de")
elem.send_keys(Keys.RETURN)
time.sleep(10)

driver.close()
