import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': "ru"})
    link = "http://selenium1py.pythonanywhere.com"
    browser = webdriver.Chrome(options=options)
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()
