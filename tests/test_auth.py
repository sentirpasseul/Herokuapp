from enum import StrEnum
from pages.auth_page import AuthPage


class AuthData(StrEnum):
    USER = "admin"
    PASSWORD = "admin"

class TestAuthPage:

    def test_auth(self, browser):
        auth_page = AuthPage()
        assert auth_page.get_alert()
        assert auth_page.auth(user=AuthData.USER, password=AuthData.PASSWORD)

