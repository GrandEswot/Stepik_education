import pytest
from selenium.common.exceptions import NoSuchElementException
import time


def should_see_add_to_basket_button(browser):
    try:
        browser.implicitly_wait(5)
        browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
        time.sleep(10)
    except NoSuchElementException:
        return False
    return True


class TestButton:

    def test_add_to_basket_button(self, browser):
        assert should_see_add_to_basket_button(browser) == True
