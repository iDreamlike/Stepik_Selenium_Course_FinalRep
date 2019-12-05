from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import CataloguePageLocators


class CataloguePage(BasePage):

    def is_adding_to_basket_accept(self, price, name):
        price_after_add = self.browser.find_element(*CataloguePageLocators.PRICE).text
        name_after_add = self.browser.find_element(*CataloguePageLocators.PRODUCT_NAME).text
        print(f"Цена товара до добавления в корзину:  {price_after_add}")
        print(f"Название товара до добавления в корзину:  {name_after_add}")
        assert price == price_after_add, "Проблема с ценой"
        assert name == name_after_add, "Проблема с названием товара"
