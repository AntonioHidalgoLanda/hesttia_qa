#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import webhelpers

import login_chef
#import login_chef.driver

# select - 
elem = login_chef.driver.find_element_by_xpath(webhelpers.xpathLink["account"])
hover = ActionChains(login_chef.driver).move_to_element(elem)
hover.perform()


# click -
elem = login_chef.driver.find_element_by_xpath(webhelpers.xpathLink["addMenu"])
elem.click()
