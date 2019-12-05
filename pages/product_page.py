from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .catalogue_page import CataloguePage


class ProductPage(BasePage):

    def add_product_to_basket(self):
        print(f"Проверяем ссылку: {self.browser.current_url}")
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        print(f"Цена товара до добавления в корзину:  {price}")
        print(f"Название товара до добавления в корзину:  {name}")
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        catalog_page = CataloguePage(browser=self.browser, url=self.browser.current_url)
        catalog_page.is_adding_to_basket_accept(price, name)
