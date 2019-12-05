from .pages.product_page import ProductPage
import pytest


big_links_list = ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9']


@pytest.mark.parametrize('links', big_links_list)
def test_guest_can_add_product_to_basket(browser, links):
    page = ProductPage(browser, links)
    page.open()
    page.add_product_to_basket()
