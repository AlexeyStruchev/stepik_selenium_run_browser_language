import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru, es, fr")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    options = Options()
    if language == 'ru':
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
        browser = webdriver.Chrome(options=options)
    if language == 'en':
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
        browser = webdriver.Chrome(options=options)
    if language == 'es':
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
        browser = webdriver.Chrome(options=options)
    if language == 'fr':
        options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
        browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()
