import selenium.webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


url = 'https://www.indeed.co.in/?r=us'
driver = webdriver.Chrome(r"mypython/bin/chromedriver_linux64/chromedriver")
driver.get(url)

driver.find_element_by_xpath('//*[@id="text-input-what"]').send_keys("teacher")
driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button').click()


items = driver.find_elements_by_xpath('//*[@id="resultsCol"]')
for item in items:
    print(item.text)