from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_LIST = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators():
    REGISTRATION_LINK = (By.ID, "registration_link")
    REGISTRATION_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_LOGIN_FIELD = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD_FIELD1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_FIELD2 = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner div.product_main h1")
    PRICE = (By.CSS_SELECTOR, "#content_inner div.product_main p.price_color")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-success:nth-child(1) div.alertinner > strong")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1)")
