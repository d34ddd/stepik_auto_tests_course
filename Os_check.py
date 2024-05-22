import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link="http://suninjuly.github.io/file_input.html"
try:
   browser = webdriver.Chrome()
   browser.get(link)   

   imya=browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
   imya.send_keys('GAVNO')

   fam=browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
   fam.send_keys('Vonuchee')

   mail=browser.find_element(By.CSS_SELECTOR, '[name="email"]')
   mail.send_keys('Zhopa@google.com')
   
   filik=browser.find_element(By.CSS_SELECTOR, '[name="file"]')    
   filik.send_keys("C:/chromedriver/Уроки/File.txt")
   
   button=browser.find_element(By.TAG_NAME,'button')
   button.click()

    

finally:
    time.sleep(10)