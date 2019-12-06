from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def is_add_product_to_basket_ok(self):
        url = self.browser.current_url
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert price == price_in_message, f"Проблема с ценами: '{price}' и '{price_in_message}' в url: {url}"
        assert name == name_in_message, f"Проблема с названиями: '{name}' и '{name_in_message}' в url: {url}"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Нет сообщения об успехе"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Успешное сообщение присутствует, но его не должно быть"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Успешное сообщение должно было исчезнуть, но не исчезло"

