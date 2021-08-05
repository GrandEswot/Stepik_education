from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')
    BASKET_ITEMS = (By.CSS_SELECTOR, 'div.basket-items')


class LoginPageLocators:
    REGISTRATION_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_EMAIL_FIELD = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM_FIELD = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.TAG_NAME, "[name='registration_submit']")


class MainPageLocators:
    BASKET = (By.CSS_SELECTOR, 'span.btn-group')


class ProductNameLocator:
    NAME = (By.CSS_SELECTOR, 'div.product_main>h1')


class ProductPageLocators:
    BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div.alert:nth-child(1) div')
    DISAPPEARANCE_ELEMENT = None


class ProductPriceLocator:
    PRICE = (By.CSS_SELECTOR, 'div.product_main>p.price_color')
