import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects1.html"


browser = webdriver.Chrome()
browser.get(link)

num1=browser.find_element(By.ID, "num1")
n11=num1.text
n1=int (n11)
num2=browser.find_element(By.ID, "num2")
n22=num2.text
n2= int (n22)
sum=n1+n2
summa=str (sum)
print ("summa =", n1, '+', n2, '=', sum)

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(summa) # ищем элемент с текстом "Python"
button=browser.find_element(By.TAG_NAME,'button')
button.click()
time.sleep(10)
