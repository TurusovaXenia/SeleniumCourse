import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_stepik_answer(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    answer_element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    )
    answer = math.log(int(time.time()) + 39.9)
    answer_str = str(answer)
    answer_element.send_keys(answer_str)
    button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    button.click()
    message_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    message_text = message_element.text
    assert message_text != "Correct!"
    print(message_text)




