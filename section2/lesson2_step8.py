"""Fill the registration form and upload a local .txt file."""

import os

from selenium import webdriver
from selenium.webdriver.common.by import By


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "lesson2_step8.txt")

browser = webdriver.Edge()
try:
    browser.get("https://suninjuly.github.io/file_input.html")
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("ivan@example.com")
    browser.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    print(browser.switch_to.alert.text, flush=True)
finally:
    browser.quit()

