import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answer_element = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_element)
    answer_element.send_keys(y)
    checkbox_element = browser.find_element(By.ID, "robotCheckbox")
    checkbox_element.click()
    radiobutton_element = browser.find_element(By.ID, "robotsRule")
    radiobutton_element.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
