from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element(By.CSS_SELECTOR, '#num1')
    num1 = a_element.text
    b_element = browser.find_element(By.CSS_SELECTOR, '#num2')
    num2 = b_element.text

    answer =str(int(num1)+int(num2))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(f'{answer}')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(16)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # не забываем оставить пустую строку в конце файла
