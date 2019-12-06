from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
            "Registration form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM),\
            "Registration form is not presented"

    def should_be_login_in_url(self):
        assert "login" in self.browser.current_url, "Can't find 'login' in current URL"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_LOGIN_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
