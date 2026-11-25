"""Read the treasure image's valuex attribute and solve the robot challenge."""

import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Edge()
try:
    browser.get("https://suninjuly.github.io/get_attribute.html")
    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")
    assert x is not None
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    print(browser.switch_to.alert.text, flush=True)
finally:
    browser.quit()

