import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"

try:
    browser.get(link)
    x_element = browser.find_element(By.ID, "num1")
    x_str = x_element.text
    x = int(x_str)
    y_element = browser.find_element(By.ID, "num2")
    y_str = y_element.text
    y = int(y_str)
    sum = x + y
    sum_str = str(sum)
    dropdown_list = Select(browser.find_element(By.ID, "dropdown"))
    dropdown_list.select_by_value(sum_str)
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()

