from .pages.main_page import MainPage
from .pages.account_page import AccountPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest
import time


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.is_basket_empty()
    page.is_message_basket_empty()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.is_basket_empty()
    page.is_message_basket_empty()


@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        page.should_be_login_in_url()


@pytest.mark.need_review_custom_scenarios
class TestMyFirstCases():

    class TestMyCasesWithGuest():
        def test_guest_can_find_product_by_using_search(self, browser):
            link = "http://selenium1py.pythonanywhere.com/"
            page = MainPage(browser, link)
            page.open()
            page.search("Google")
            page.search_result_check("Google")

    class TestMyCasesWithUser():
        @pytest.fixture(scope="function", autouse=True)
        def setup(self, browser):
            link = "http://selenium1py.pythonanywhere.com/accounts/login/"
            page = LoginPage(browser, link)
            page.open()
            email = str(time.time()) + "@fakemail.org"
            password = 'Qq111111Qq'
            page.register_new_user(email, password)
            page.should_be_authorized_user()

        def test_user_can_create_new_address(self, browser):
            link = "http://selenium1py.pythonanywhere.com/"
            page = AccountPage(browser, link)
            page.open()
            page.go_to_account()
            page.go_to_address_book()
            page.add_new_address()
