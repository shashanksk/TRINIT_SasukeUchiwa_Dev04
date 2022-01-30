from ast import Delete
from distutils.command.build_scripts import first_line_re
from itertools import dropwhile
from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from datetime import datetime
# for implicit and explict waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options  # for suppressing the browser


now = datetime.now()

current_time = now.strftime("%H:%M:%S")


print("ENTER THE EMAIL-ADDRESS TO SEARCH THE PROFILE ::")
email = input()

driver = webdriver.Chrome()

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--headless")

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


time.sleep(8)

# newContactButton = driver.find_element_by_xpath(
#     '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/span/button[1]')
# newContactButton.click()
# newContactButton.click()
# newContactButton.click()
# newContactButton.click()

# DeleteExistingContact = driver.find_element_by_xpath(
#     '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[5]/button/span')
# DeleteExistingContact.click()
# time.sleep(10)

# deleteConfirmation = driver.find_element_by_xpath(
#     '/html/body/div[8]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/span[1]/button/span')
# deleteConfirmation.click()

# full x path /html/body/div[8]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/span[1]/button

time.sleep(10)

# this is to test the button be aware
# newContactButton = driver.find_element_by_xpath(
#     '/html/body/div[3]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/ul/li[2]/ul/button[1]')

newContactButton = driver.find_element_by_xpath(
    '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/span/button[1]')


newContactButton.click()

time.sleep(6)
# addNewContactButton = driver.find_element_by_xpath(
#     '/html/body/div[3]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/button[1]')
# addNewContactButton.click()

time.sleep(3)
firstNameBox = driver.find_element_by_xpath(
    '/html/body/div[8]/div/div/div/div[2]/div[2]/main/section[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/input')
firstNameBox.send_keys(current_time)

addMoredropDown = driver.find_element_by_xpath(
    '/html/body/div[8]/div/div/div/div[2]/div[2]/main/section[2]/div[2]/div/button[3]/span')
addMoredropDown.click()

addEmail = driver.find_element_by_xpath(
    '/html/body/div[9]/div/div/div/div/div/div/ul/li[1]/button ')
addEmail.click()

enteringEmail = driver.find_element_by_xpath(
    '/html/body/div[8]/div/div/div/div[2]/div[2]/main/section[2]/div[1]/div/fieldset[1]/div[1]/div/div/div/div[2]/input')
enteringEmail.send_keys(email)

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

# get current window handle
p = driver.current_window_handle

# get first child window
chwd = driver.window_handles

for w in chwd:
    # switch focus to child window
    if(w != p):
        driver.switch_to.window(w)

print("\n\n\n\nlinkedIn profile url::")

print(driver.current_url)
print('\n\ndone')

driver.close()
driver.quit()
