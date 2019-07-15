#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from Hesttia import Hesttia, landingPage

driver = webdriver.Firefox()
driver.get(landingPage)
hesttia = Hesttia(driver)
hesttia.login(hesttia)

time.sleep(5)
hesttia.clickSubMenuXpathKey("account", "addMenu")


