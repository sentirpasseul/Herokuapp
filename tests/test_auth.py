from pages.auth_page import AuthPage
from config.urls import URLs
from data.auth_data import DataAuth


class TestAuth:

    def test_auth(self, browser):
        auth_page = AuthPage(browser)
        browser.get(f"https://{DataAuth.USER}:{DataAuth.PASSWORD}@" + URLs.BASIC_AUTH_URL)
        auth_page.wait_for_open()
        assert auth_page.is_success_message_exists(), "Ошибка при проверке видимости успешного сообщения"
