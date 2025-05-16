import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # Нажать на кнопку (откроется новая вкладка)
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Решить капчу на новой странице
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Ввести ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Нажать кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Получить результат из алерта
    alert = browser.switch_to.alert
    alert_text = alert.text
    print("Результат:", alert_text.split()[-1])
    alert.accept()

finally:
    # Закрыть браузер
    browser.quit()