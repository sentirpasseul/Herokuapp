from pages.windows_page import WindowsPage
from config.urls import URLs
from enum import StrEnum


class TestData(StrEnum):
    TEXT_NEW_PAGE = "New Window"
    TITLE_NEW_PAGE = "New Window"


class TestWindows:

    def test_windows_page(self, browser):
        browser.get(url=URLs.WINDOWS_PAGE)
        windows_page = WindowsPage(browser)
        assert windows_page.wait_for_open(), "Ошибка при открытии страницы Windows Page"
        assert windows_page.check_link(), "Ошибка при проверке ссылки Click Here"
        assert windows_page.check_open_new_tab(label=TestData.TEXT_NEW_PAGE, title=TestData.TITLE_NEW_PAGE), (
            "Ошибка при проверки открытия новой вкладки")
        assert windows_page.check_return_to_original_page(), "Ошибка при переключении на начальную вкладку"
        assert windows_page.check_link(), "Ошибка при проверке ссылки Click Here"
        assert windows_page.check_open_new_tab(label=TestData.TEXT_NEW_PAGE, title=TestData.TITLE_NEW_PAGE), (
            "Ошибка при проверки открытия новой вкладки")
        assert windows_page.check_close_tabs(), "Ошибка при проверке закрытия всех вкладок кроме первоначальной"
