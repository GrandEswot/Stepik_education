from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Product in basket present, but basket should be empty"

    def should_not_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Basket is empty, but should be not"
