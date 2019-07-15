#!/usr/bin/python
from selenium import webdriver
import time
from Hesttia import Hesttia, landingPage

driver = webdriver.Firefox()
driver.get(landingPage)
hesttia = Hesttia(driver)
hesttia.login(hesttia)

time.sleep(10)
driver.close()


