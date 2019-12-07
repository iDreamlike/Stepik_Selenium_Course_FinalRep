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
        Select(self.browser.find_element_by_id("id_title")).select_by_value("Mr")
        self.browser.find_element(By.ID, "id_first_name").send_keys("Иван")
        self.browser.find_element(By.ID, "id_last_name").send_keys("Иванов")
        self.browser.find_element(By.ID, "id_line1").send_keys("Адрес7")
        self.browser.find_element(By.ID, "id_line2").send_keys("Адрес2")
        self.browser.find_element(By.ID, "id_line3").send_keys("Адрес3")
        self.browser.find_element(By.ID, "id_line4").send_keys("Город")
        self.browser.find_element(By.ID, "id_state").send_keys("Область")
        self.browser.find_element(By.ID, "id_postcode").send_keys("190000")
        Select(self.browser.find_element_by_id("id_country")).select_by_value("RU")
        self.browser.find_element(By.ID, "id_phone_number").send_keys("8123270000")
        self.browser.find_element(By.ID, "id_notes").send_keys("Тестовые инструкции")
        self.browser.find_element(By.CSS_SELECTOR, ".col-sm-offset-4 button").click()
        assert self.is_element_present(By.CSS_SELECTOR, "#messages .alert-success")
