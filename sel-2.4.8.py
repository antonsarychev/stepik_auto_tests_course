from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "book")))
    button.click()

    x = browser.find_element(By.ID, 'input_value').text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    input_text = browser.find_element(By.ID, "answer")
    input_text.send_keys(y)

    button_submit = browser.find_element(By.ID, "solve")
    button_submit.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

'''    
# лучше избегать time.sleep(5) в автотестах, и пользоваться неявными и явными ожиданиями WebDriver (Implicit и Explicit Waits)
browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд, пока они не появятся на веб-странице
browser.implicitly_wait(5)'''

'''
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
button.click()'''