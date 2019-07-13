#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import webhelpers

userData = {
    "username": "hesttia.infochef001",
    "password": "mLxBsAXVe#Pe"
}

formField = {
    "username": "username",
    "password": "password",
    'submit': "login"
}

driver = webdriver.Firefox()
driver.get(webhelpers.landingPage)

elem = driver.find_element_by_xpath(webhelpers.xpathLink["login"])
elem.click()

webhelpers.updateField(driver, formField["username"], userData["username"])
webhelpers.updateField(driver, formField["password"], userData["password"])

webhelpers.submit(driver, formField["submit"])

time.sleep(10)
driver.close()


