import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistartionForm(unittest.TestCase):

    def test_registration_form1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        firstname = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.first_class input")
        firstname.send_keys("Xenia")

        lastname = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.second_class input")
        lastname.send_keys("Turusova")

        email = browser.find_element(By.CLASS_NAME, "form-control.third")
        email.send_keys("kseniya6665@gmail.com")

        button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "text is incorrect")

    def test_registration_form2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        firstname = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.first_class input")
        firstname.send_keys("Xenia")

        lastname = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.second_class input")
        lastname.send_keys("Turusova")

        email = browser.find_element(By.CLASS_NAME, "form-control.third")
        email.send_keys("kseniya6665@gmail.com")

        button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "text is incorrect")
