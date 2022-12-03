import math
import time
import os 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(2)

    x = browser.find_element(By.CSS_SELECTOR,"span#input_value").text
    result = calc(x)

    input_field = browser.find_element(By.ID,"answer")
    input_field.send_keys(result)

    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    time.sleep(10)
    browser.quit()
	