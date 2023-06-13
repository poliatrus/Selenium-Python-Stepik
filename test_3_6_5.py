import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize('link_answer', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_answer(browser, link_answer):
    link = f"https://stepik.org/lesson/{link_answer}/step/1"
    browser.get(link)
    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#ember33"), 'Войти')
    )
    browser.find_element(By.CSS_SELECTOR, "#ember33").click()
    time.sleep(1)
    # вводим логин и пароль
    browser.find_element(By.CSS_SELECTOR,"[name = 'login']").send_keys('')
    browser.find_element(By.CSS_SELECTOR, "[name = 'password']").send_keys('')
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    time.sleep(6)

    answer = math.log(int(time.time()))
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Напишите ваш ответ здесь...']").send_keys(str(answer))
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"), )
    )
    browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()
    time.sleep(6)

    # Проверка на текст ответа
    corrector = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    assert corrector == 'Correct!'
