import time

from selenium.webdriver.common.by import By


def test_add_to_cart_button_exists(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(10)
    add_to_cart_button = browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    assert add_to_cart_button.is_displayed()
