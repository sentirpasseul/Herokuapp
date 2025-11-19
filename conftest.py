from core.browser_factory import BrowserFactory
from core.browser import Browser
import pytest

DEFAULT_LINK = "http://the-internet.herokuapp.com"

@pytest.fixture(scope='function')
def browser():
    driver = BrowserFactory.get_driver()
    browser = Browser(driver=driver)
    browser.get(DEFAULT_LINK)
    yield browser
    browser.quit()


