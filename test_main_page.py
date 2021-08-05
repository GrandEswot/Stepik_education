import time

import pytest

from .pages.links import ProductPageLink
from .pages.locators import BasketPageLocators
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    @pytest.mark.setup
    def test_should_be_register_new_user(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = '!123456789Q'
        page = LoginPage(browser)
        page.open_page(ProductPageLink.LINK)
        page.go_to_login_page()
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        with open('log/users_data.log', 'a') as file:
            user_data = {
                'email': email,
                'password': password
            }
            file.write(str(user_data) + '\n')

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser)
        page.open_page(link)
        page.go_to_login_page()
        page.should_be_login_link()
        login_page = LoginPage(browser)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser)
        page.open_page('http://selenium1py.pythonanywhere.com')
        page.go_to_basket_page()
        page.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
        page.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
