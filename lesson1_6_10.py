from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

#   Вариант 1
#   xpath = "//label[contains(text(), '*')]/following-sibling::input"  поиск * в родительском элементе
#   input_list = browser.find_elements_by_xpath(xpath)
#   output_list = ['First_name', 'Last_name', 'test@mail.ru']
#   for element, data in zip(input_list, output_list):
#       element.send_keys(data)

    labels = browser.find_elements(By.TAG_NAME, 'label')  # Список лэйблов над текстовыми полями
    inputs = browser.find_elements(By.TAG_NAME, 'input')  # Список текстовых полей

    # Заполняет обязательные поля
    for i, label in enumerate(labels):
        if label.text == 'First name*':
            inputs[i].send_keys('Ivan')
        elif label.text == 'Last name*':
            inputs[i].send_keys('Ivanov')
        elif label.text == 'Email*':
            inputs[i].send_keys('test@mail.ru')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    #Какой текст проверяем?
    text = "Congratulations! You have successfully registered!"

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text
    assert text == welcome_text, f'Expected text {text}, but got {welcome_text}'

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # не забываем оставить пустую строку в конце файла
