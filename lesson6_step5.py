import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()

try:
    browser.get(link)
    result = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    link = browser.find_element(By.LINK_TEXT, result)
    link.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Xenia")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Turusova")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Krasnoyarsk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
