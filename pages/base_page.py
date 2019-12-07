from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
# from .locators import MainPageLocators


class BasePage():
    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_account(self):
        account_link = self.browser.find_element(*BasePageLocators.ACCOUNT_LINK)
        account_link.click()

    def go_to_basket(self):
        button = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON)
        button.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def open(self):
        self.browser.get(self.url)

    def search(self, product_to_find):
        text_area = self.browser.find_element(*BasePageLocators.SEARCH_FIELD)
        text_area.clear()
        text_area.send_keys(product_to_find)
        button = self.browser.find_element(*BasePageLocators.SEARCH_BUTTON)
        button.click()

    def search_result_check(self, product_to_check):
        result_of_seek = self.browser.find_element(*BasePageLocators.SEARCH_RESULT_PRODUCT_NAME).text
        assert product_to_check in result_of_seek,\
            "Название найденного товара не совпадает с тестируемым"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
            pass

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK),\
            "Login link is not presented"
