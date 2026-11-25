"""Use execute_script to bring the covered form into view before submission."""

import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Edge()
try:
    browser.get("https://suninjuly.github.io/execute_script.html")
    x = browser.find_element(By.ID, "input_value").text
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    for element_id in ("robotCheckbox", "robotsRule"):
        control = browser.find_element(By.ID, element_id)
        browser.execute_script("return arguments[0].scrollIntoView(true);", control)
        control.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    print(browser.switch_to.alert.text, flush=True)
finally:
    browser.quit()

