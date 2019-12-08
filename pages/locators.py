from selenium.webdriver.common.by import By


class AccountPageLocators():
    ADDRESS_BOOK_LINK = (By.CSS_SELECTOR, ".page_inner aside.sidebar > ul > li:nth-child(3) > a")
    ADD_NEW_ADDRESS_BUTTON = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > div > div > p > a")
    ADD_NEW_ADDRESS_TITLE_FIELD = (By.ID, "id_title")
    ADD_NEW_ADDRESS_FIRST_NAME_FIELD = (By.ID, "id_first_name")
    ADD_NEW_ADDRESS_LAST_NAME_FIELD = (By.ID, "id_last_name")
    ADD_NEW_ADDRESS_FIRST_LINE_ADDR_FIELD = (By.ID, "id_line1")
    ADD_NEW_ADDRESS_SECOND_LINE_ADDR_FIELD = (By.ID, "id_line2")
    ADD_NEW_ADDRESS_THIRD_LINE_ADDR_FIELD = (By.ID, "id_line3")
    ADD_NEW_ADDRESS_CITY_FIELD = (By.ID, "id_line4")
    ADD_NEW_ADDRESS_STATE_FIELD = (By.ID, "id_state")
    ADD_NEW_ADDRESS_ZIP_FIELD = (By.ID, "id_postcode")
    ADD_NEW_ADDRESS_COUNTRY_FIELD = (By.ID, "id_country")
    ADD_NEW_ADDRESS_PHONE_FIELD = (By.ID, "id_phone_number")
    ADD_NEW_ADDRESS_INSTRUCTIONS_FIELD = (By.ID, "id_notes")
    ADD_NEW_ADDRESS_SAVE_BUTTON = (By.CSS_SELECTOR, ".col-sm-offset-4 button")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#browse + form input.btn")
    SEARCH_FIELD = (By.ID, "id_q")
    SEARCH_RESULT_PRODUCT_NAME = (By.CSS_SELECTOR, "section > div > ol > li > article > h3 > a")
    ACCOUNT_LINK = (By.CSS_SELECTOR, "#top_page ul > li:nth-child(1) > a")


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
