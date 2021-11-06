import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()

try:
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Ответ")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
finally:
    time.sleep(30)
    browser.quit()

