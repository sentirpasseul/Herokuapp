from pages.auth_page import AuthPage
from config.urls import URLs


class TestAuth:
    USER = "admin"
    PASSWORD = "admin"

    def test_auth(self, browser):
        auth_page = AuthPage(browser)
        auth_page.auth(user=self.USER, password=self.PASSWORD)
        assert auth_page.open(), "Ошибка при попытке открытия страницы с успешной авторизацией \n"
        assert auth_page.is_auth_success(), "Ошибка при попытке отображения текста с успешной авторизацией \n"
