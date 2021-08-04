from .pages.locators import MainPageLocators, BasketPageLocators
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser)
    page.open_page(link)
    page.go_to_login_page()
    page.should_be_login_link()
    login_page = LoginPage(browser)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser)
    page.open_page('http://selenium1py.pythonanywhere.com')
    page.go_to_basket_page()
    page.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
    page.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)


