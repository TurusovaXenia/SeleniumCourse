import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answer_element = browser.find_element(By.ID, "answer")
    answer_element.send_keys(y)
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()

