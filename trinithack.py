from lib2to3.pgen2 import driver
import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://youtube.com')

time.sleep(7)

print("sleep done")

search_box = driver.find_element_by_xpath(
    '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')

# sleep(5)

search_box.send_keys('221 ENIGMA')

search_button = driver.find_element_by_xpath(
    '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button')

search_button.click()

time.sleep(3)

play_first = driver.find_element_by_xpath(
    '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]')
play_first.click()

print("no issues")
