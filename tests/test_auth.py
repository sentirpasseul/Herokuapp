from enum import StrEnum
from pages.auth_page import AuthPage


class AuthData(StrEnum):
    USER = "admin"
    PASSWORD = "admin"

class TestAuth:

    def test_auth(self, browser):
        auth_page = AuthPage(browser)
        assert auth_page.auth(user=AuthData.USER, password=AuthData.PASSWORD)
        assert auth_page.wait_for_open()
        assert auth_page.auth_success()

