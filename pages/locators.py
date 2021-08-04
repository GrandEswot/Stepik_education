from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    REGISTRATION_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")


class ProductNameLocator:
    NAME = (By.CSS_SELECTOR, 'div.product_main>h1')


class ProductPageLocators:
    BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div.alert:nth-child(1) div')
    DISAPPEARANCE_ELEMENT = None


class ProductPriceLocator:
    PRICE = (By.CSS_SELECTOR, 'div.product_main>p.price_color')
