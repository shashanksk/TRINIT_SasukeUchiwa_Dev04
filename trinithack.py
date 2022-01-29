from distutils.command.build_scripts import first_line_re
from itertools import dropwhile
from lib2to3.pgen2 import driver
import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://outlook.com')

signInButton = driver.find_element_by_xpath(
    '/html/body/header/div/aside/div/nav/ul/li[2]/a')

signInButton.click()

emailBox = driver.find_element_by_xpath(
    '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]')

emailBox.send_keys('sasukeuchiwa0825@outlook.com')

time.sleep(3)

nextButton = driver.find_element_by_xpath(
    '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input')
nextButton.click()

time.sleep(3)

passwordBox = driver.find_element_by_xpath(
    '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input')
passwordBox.send_keys('shennibinni69')

nextButtonInpassword = driver.find_element_by_xpath(
    '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input')
nextButtonInpassword.click()

staySignedButton = driver.find_element_by_xpath(
    '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input')
staySignedButton.click()

time.sleep(2)

clickOntheContactsbutton = driver.find_element_by_xpath(
    '/html/body/div[3]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[3]/div/button')
clickOntheContactsbutton.click()


time.sleep(15)

# newContactButton = driver.find_element_by_xpath(
#     '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/span/button[1]')
# newContactButton.click()
# newContactButton.click()
# newContactButton.click()
# newContactButton.click()

newContactButton = driver.find_element_by_xpath(
    '/html/body/div[3]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/ul/li[2]/ul/button[1]')

newContactButton.click()

time.sleep(10)
addNewContactButton = driver.find_element_by_xpath(
    '/html/body/div[3]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/button[1]')

addNewContactButton.click()

firstNameBox = driver.find_element_by_xpath(
    '/html/body/div[8]/div/div/div/div[2]/div[2]/main/section[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/input')
firstNameBox.send_keys('xvy')

addMoredropDown = driver.find_element_by_xpath(
    '/html/body/div[8]/div/div/div/div[2]/div[2]/main/section[2]/div[2]/div/button[3]/span')
addMoredropDown.click()

addEmail = driver.find_element_by_xpath(
    '/html/body/div[9]/div/div/div/div/div/div/ul/li[1]/button ')
addEmail.click()

enteringEmail = driver.find_element_by_xpath(
    '/html/body/div[8]/div/div/div/div[2]/div[2]/main/section[2]/div[1]/div/fieldset[1]/div[1]/div/div/div/div[2]/input')
enteringEmail.send_keys('shannoncarlo2561@gmail.com')

createButtonForContact = driver.find_element_by_xpath(
    '/html/body/div[8]/div/div/div/div[2]/div[2]/main/section[2]/div[2]/div/button[1]')
createButtonForContact.click()

time.sleep(5)
clickOnthebloodylinkedin = driver.find_element_by_xpath(
    '/html/body/div[3]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/div[1]/div[2]/div/button[4]')
clickOnthebloodylinkedin.click()

time.sleep(2)
finalButtonToLinkedIn = driver.find_element_by_xpath(
    '/html/body/div[3]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/div[2]/section/div[2]/button')
finalButtonToLinkedIn.click()

time.sleep(10)

urlfirst = driver.find_element_by_xpath(
    '//*[@id="main-content"]/div/h1/strong')

print(urlfirst)


print('done')
