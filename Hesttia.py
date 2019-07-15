from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

landingPage = "https://beta.hesttia.com"

xpathLink = {
    "signup": "//*[@id='menu-item-342']//a",
    "login": "//*[@id='menu-item-219']//a",
    "account": "//*[@id='menu-item-215']//a",
    "addMenu": "//*[@id='menu-item-251']//a"
}

loginData = {
    "username": "hesttia.infochef001",
    "password": "mLxBsAXVe#Pe"
}

loginField = {
    "username": "username",
    "password": "password",
    'submit': "login"
}

class Hesttia:
    def __init__(self, driver):
        self.driver = driver

    def updateField(self, field, value):
        elem = self.driver.find_element_by_id(field)
        elem.clear();
        elem.send_keys(value)
    
    def submit(self, field):
        elem = self.driver.find_element_by_name(field)
        elem.send_keys(Keys.RETURN)

    def clickMenuXpathKey(self, xpathKey):
        elem = self.driver.find_element_by_xpath(xpathLink[xpathKey])
        elem.click()
        
    def clickSubMenuXpathKey(self, xpathKey1, xpathKey2):
        # hover
        elem = self.driver.find_element_by_xpath(xpathLink[xpathKey1])
        hover = ActionChains(self.driver).move_to_element(elem)
        hover.perform()
        # click
        elem = self.driver.find_element_by_xpath(xpathLink[xpathKey2])
        elem.click()

    def login(self, userData):
        self.clickMenuXpathKey("login")
        self.updateField(loginField["username"], loginData["username"])
        self.updateField(loginField["password"], loginData["password"])
        self.submit(loginField["submit"])
        