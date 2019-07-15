#!/usr/bin/python
from selenium import webdriver
import time
from Hesttia import Hesttia, landingPage

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
driver.get(landingPage)
hesttia = Hesttia(driver)

hesttia.clickMenuXpathKey("signup")

hesttia.updateField(inputUser["firstName"],dataUser["firstName"])
hesttia.updateField(inputUser["lastName"],dataUser["lastName"])
hesttia.updateField(inputUser["email"],dataUser["email"])
hesttia.updateField(inputUser["cert"],dataUser["cert"])
hesttia.updateField(inputUser["bio"],dataUser["bio"])

hesttia.submit(inputUser["submit"])

time.sleep(10)
driver.close()

#print(dataUser)