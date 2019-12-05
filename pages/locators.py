from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#registration_link")
    REGISTRATION_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner div.product_main h1")
    PRICE = (By.CSS_SELECTOR, "#content_inner div.product_main p.price_color")


class CataloguePageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div.alert-success:nth-child(1) div.alertinner > strong")
    PRICE = (By.CSS_SELECTOR, "#messages div.alertinner p strong")
