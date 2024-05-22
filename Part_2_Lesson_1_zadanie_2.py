import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.TAG_NAME, "img")
    x_number=x_element.get_attribute('valuex')
    x = x_number
    y=calc(x)
    pole=browser.find_element(By.ID, "answer")
    pole.send_keys(y)
    checkbox=browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    option1=browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option1.click()
    button=browser.find_element(By.TAG_NAME,'button')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()