from .pages.login_page import LoginPage


def test_guest_login_set(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.should_be_register_form()
    page.should_be_login_link()
