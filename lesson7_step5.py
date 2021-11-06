import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answer_element = browser.find_element(By.ID, "answer")
    answer_element.send_keys(y)
    checkbox_element = browser.find_element(By.ID, "robotCheckbox")
    checkbox_element.click()
    radiobutton_element = browser.find_element(By.ID, "robotsRule")
    radiobutton_element.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
