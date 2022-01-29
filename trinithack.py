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

print("no issues")
