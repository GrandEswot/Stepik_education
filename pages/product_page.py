from .base_page import BasePage
from .locators import *


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET)
        basket_button.click()

    def name_assert(self):
        product_name = self.browser.find_element(*ProductNameLocator.NAME)
        product_name_text = product_name.text
        product_name_field = self.browser.find_element(By.CSS_SELECTOR, '#messages div.alert:nth-child(1) div').text
        assert product_name_text in product_name_field

    def price_assert(self):
        product_price = self.browser.find_element(*ProductPriceLocator.PRICE)
        product_price_value = product_price.text
        product_price_field = self.browser.find_element(By.CSS_SELECTOR, 'div.basket-mini').text
        assert product_price_value in product_price_field

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_element_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Element is still present, but should be disappear"
