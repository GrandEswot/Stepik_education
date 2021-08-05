from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
from .main_page import MainPage


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        password_verify_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM_FIELD)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_verify_field.send_keys(password)
        registration_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, \
            "Login link does not much"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), \
            "Registration for not presented"
