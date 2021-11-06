import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    checkbox_element = browser.find_element(By.ID, "robotCheckbox")
    checkbox_element.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()