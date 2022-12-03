from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math

def sum_function(a, b):
  return str(int(a) + int(b))

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = browser.find_element(By.ID,"num1").text
    num_2 = browser.find_element(By.ID,"num2").text
    
    result = sum_function(num_1, num_2)

    select = Select(browser.find_element(By.TAG_NAME,"select"))
    select.select_by_visible_text(result)

    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
