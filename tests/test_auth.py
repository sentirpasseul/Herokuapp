from pages.auth_page import AuthPage
from config.urls import URLs


class TestAuth:
    USER = "admin"
    PASSWORD = "admin"

    def test_auth(self, browser):
        auth_page = AuthPage(browser)
        browser.get(f"https://{TestAuth.USER}:{TestAuth.PASSWORD}@" + URLs.BASIC_AUTH_URL)
        auth_page.wait_for_open()
        auth_page.wait_for_success_message()
