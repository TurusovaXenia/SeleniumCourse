import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()

try:
    browser.get(link)
    firstname_element = browser.find_element(By.NAME, "firstname")
    firstname_element.send_keys("Xenia")
    lastname_element = browser.find_element(By.NAME, "lastname")
    lastname_element.send_keys("Turusova")
    email_element = browser.find_element(By.NAME, "email")
    email_element.send_keys("kse@gmail.com")
    file_button = browser.find_element(By.ID, "file")
    file_path = "C:\chromedriver\Doc.txt"
    file_button.send_keys(file_path)
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()

