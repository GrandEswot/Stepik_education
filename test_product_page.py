import pytest
import time

from pages.locators import MainPageLocators, BasketPageLocators
from .pages.ProductPage import ProductPage
from .pages.links import ProductPageLink


@pytest.mark.parametrize('link', [
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
                                               "?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                  ])
def test_add_product_to_basket(browser, link):
    product_page = ProductPage(browser)
    product_page.open_page(link)
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.name_assert()
    product_page.price_assert()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser)
    page.open_page(link)
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser)
    page.open_page(link)
    page.go_to_basket_page()
    page.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
    page.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser)
    product_page.open_page(ProductPageLink.LINK)
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser)
    product_page.open_page(ProductPageLink.LINK)
    product_page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser)
    page.open_page(link)
    page.should_be_login_link()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser)
    product_page.open_page(ProductPageLink.LINK)
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_element_is_disappeared()
