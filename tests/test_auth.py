from pages.auth_page import AuthPage
from config.urls import URLs
from data.auth_data import TestDataAuth

class TestAuth:

    def test_auth(self, browser):
        auth_page = AuthPage(browser)
        browser.get(f"https://{TestDataAuth.USER}:{TestDataAuth.PASSWORD}@" + URLs.BASIC_AUTH_URL)
        auth_page.wait_for_open()
        assert auth_page.is_success_message_visible(), "Ошибка при проверке видимости успешного сообщения"
