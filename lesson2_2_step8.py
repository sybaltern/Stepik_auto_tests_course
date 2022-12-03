import math
import time
import os 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    first_name = browser.find_element(By.CSS_SELECTOR,"input[name='firstname']")
    first_name.send_keys("Nikita")

    last_name = browser.find_element(By.CSS_SELECTOR,"input[name='lastname']")
    last_name.send_keys("Ivanov")

    email_field = browser.find_element(By.CSS_SELECTOR,"input[name='email']")
    email_field.send_keys("123@contoso.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')

    file_field = browser.find_element(By.CSS_SELECTOR,"[type='file']")
    file_field.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
   