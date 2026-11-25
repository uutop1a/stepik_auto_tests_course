"""Switch to the newly opened browser tab and solve its challenge."""

import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Edge()
try:
    browser.get("https://suninjuly.github.io/redirect_accept.html")
    browser.find_element(By.TAG_NAME, "button").click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    print(browser.switch_to.alert.text, flush=True)
finally:
    browser.quit()

