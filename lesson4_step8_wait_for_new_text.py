from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element_by_id("book")
    element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()

    x_element = browser.find_element_by_id("input_value")
    x_ = x_element.text
    y = calc(x_)
    element = browser.find_element_by_id("answer")
    element.send_keys(y)
    button = browser.find_element_by_id("solve")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    res = alert_text.split(': ')[-1]
    print(res)
finally:
    time.sleep(7)
    browser.quit()
