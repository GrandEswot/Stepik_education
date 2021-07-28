import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru/en-gb/es/fr")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.get(f'https://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/')
    # try:
    #     print("\nOpen browser page with chosen language version")
    #     browser.get(f'https://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/')
    # except:
    #     raise pytest.UsageError("--language should be ru/en-gb/es/fr")
    yield browser
    print("\nquit browser..")
    browser.quit()
