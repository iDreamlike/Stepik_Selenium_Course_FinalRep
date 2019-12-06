from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_basket_empty(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCT_LIST),\
            "Список товаров присутствует, но не должен"

    def is_message_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY),\
            "Нет сообщения о том, что корзина пуста"
