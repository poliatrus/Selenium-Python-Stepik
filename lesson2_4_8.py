from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import os

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price_wait = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    answer = alert_text.split(': ')[-1]
    time.sleep(1)
    alert.accept()
    # Ответ задачи распечтать
    print(answer)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
    # не забываем оставить пустую строку в конце файла