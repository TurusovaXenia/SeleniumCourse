import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
broswer = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    broswer.get(link)
    magic_button = broswer.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
    magic_button.click()
    new_window = broswer.window_handles[1]
    broswer.switch_to.window(new_window)
    x_element = broswer.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answer_element = broswer.find_element(By.ID, "answer")
    answer_element.send_keys(y)
    submit_button = broswer.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit_button.click()
finally:
    time.sleep(30)
    broswer.quit()