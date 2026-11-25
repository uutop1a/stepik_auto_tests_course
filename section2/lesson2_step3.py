"""Select the sum in a dropdown on either version of the exercise page."""

import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


url = sys.argv[1] if len(sys.argv) > 1 else "https://suninjuly.github.io/selects1.html"
browser = webdriver.Edge()
try:
    browser.get(url)
    first = int(browser.find_element(By.ID, "num1").text)
    second = int(browser.find_element(By.ID, "num2").text)
    Select(browser.find_element(By.ID, "dropdown")).select_by_value(str(first + second))
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    print(browser.switch_to.alert.text, flush=True)
finally:
    browser.quit()

