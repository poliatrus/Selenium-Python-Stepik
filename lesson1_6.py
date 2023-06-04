from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(by='tag name',value='input')
    print(input1)
    input1.send_keys("Ivan")
    input2 = browser.find_element(by='name', value='last_name')
    print(input2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(by='class name', value='orm-control city')
    print(input3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element(by='id', value='country')
    print(input4)
    input4.send_keys("Russia")
    button = browser.find_element(by='css selector', value="button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


# Вариант 2
input1 = browser.find_elements_by_xpath("//input")[0]
input1.send_keys("Ivan")
input2 = browser.find_elements_by_xpath("//input")[1]
input2.send_keys("Petrov")
input3 = browser.find_elements_by_xpath("//input")[2]
input3.send_keys("Smolensk")
input4 = browser.find_elements_by_xpath("//input")[3]
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()