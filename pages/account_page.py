from .locators import AccountPageLocators
from .base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AccountPage(BasePage):

    def go_to_address_book(self):
        address_book_link = self.browser.find_element(*AccountPageLocators.ADDRESS_BOOK_LINK)
        address_book_link.click()

    def add_new_address(self):
        add_new_address_button = self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS_BUTTON)
        add_new_address_button.click()
        Select(self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS_TITLE_FIELD)).select_by_value("Mr")
        self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS_FIRST_NAME_FIELD).send_keys("Иван")
        self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS_LAST_NAME_FIELD).send_keys("Иванов")
        self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS_FIRST_LINE_ADDR_FIELD).send_keys("Адрес7")
        self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS_SECOND_LINE_ADDR_FIELD).send_keys("Адрес2")
        self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS_THIRD_LINE_ADDR_FIELD).send_keys("Адрес3")
        self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS_CITY_FIELD).send_keys("Город")
        self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS_STATE_FIELD).send_keys("Область")
        self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS_ZIP_FIELD).send_keys("190000")
        Select(self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS_COUNTRY_FIELD)).select_by_value("RU")
        self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS_PHONE_FIELD).send_keys("8123270000")
        self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS_INSTRUCTIONS_FIELD).send_keys("Тестовые инструкции")
        self.browser.find_element(*AccountPageLocators.ADD_NEW_ADDRESS_SAVE_BUTTON).click()
        assert self.is_element_present(By.CSS_SELECTOR, "#messages .alert-success")
