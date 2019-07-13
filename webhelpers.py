from selenium.webdriver.common.keys import Keys

landingPage = "https://beta.hesttia.com"

xpathLink = {
    "signup": "//*[@id='menu-item-342']//a",
    "login": "//*[@id='menu-item-219']//a"
}


def updateField(driver, field, value):
    elem = driver.find_element_by_id(field)
    elem.clear();
    elem.send_keys(value)

def submit(driver, field):
    elem = driver.find_element_by_name(field)
    elem.send_keys(Keys.RETURN)
