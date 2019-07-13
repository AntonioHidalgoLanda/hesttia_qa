#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import webhelpers

inputUser = {
    'firstName': "reg_sr_firstname",
    'lastName': "reg_sr_lastname",
    'email': "reg_email",
    'cert': "reg_billing_certificacion_(e.g._carnet_de_manipulador_de_alimentos)",
    'bio': "reg_billing_biografia",
    'submit': "register"
}

dataUser = {
    'firstName': "Jerome",
    'lastName': "McElroy",
    'email': "hesttia.info+chef001@gmail.com",
    'cert': "THIS_IS_A_TEST_201907102227_CHEF001",
    'bio': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam accumsan dignissim neque, sed congue leo accumsan ultrices. Curabitur auctor cursus lacus, ac tincidunt sapien sodales in. Morbi tristique tellus ex, in lacinia mi facilisis at. Phasellus et tincidunt est. Cras ornare quam id arcu pellentesque, sed tincidunt nibh aliquam. Mauris sed sagittis sem, nec euismod tellus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam arcu mauris, luctus sit amet nisi vestibulum, rutrum egestas mi."
}

driver = webdriver.Firefox()
driver.get(webhelpers.landingPage)

elem = driver.find_element_by_xpath(webhelpers.xpathLink["signup"])
elem.click()

webhelpers.updateField(driver,inputUser["firstName"],dataUser["firstName"])
webhelpers.updateField(driver,inputUser["lastName"],dataUser["lastName"])
webhelpers.updateField(driver,inputUser["email"],dataUser["email"])
webhelpers.updateField(driver,inputUser["cert"],dataUser["cert"])
webhelpers.updateField(driver,inputUser["bio"],dataUser["bio"])

webhelpers.submit(driver, inputUser["submit"])

time.sleep(10)
driver.close()

#print(dataUser)