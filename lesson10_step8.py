import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser.get(link)
book_button = browser.find_element(By.ID, "book")

button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

book_button.click()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

answer_element = browser.find_element(By.ID, "answer")
answer_element.send_keys(y)

submit_button = browser.find_element(By.ID, "solve")
submit_button.click()
