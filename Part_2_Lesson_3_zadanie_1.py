import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link='http://suninjuly.github.io/redirect_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

knopka=browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
knopka.click()

first_window = browser.window_handles[0]
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y=calc(x)

pole=browser.find_element(By.ID, "answer")
pole.send_keys(y)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(10)