from enum import StrEnum
from config.urls import URLs

from pages.context_menu_page import ContextMenuPage


class TestDataContextMenu(StrEnum):
    TEST_ALERT_TEXT = "You selected a context menu"


class TestContextMenu:

    def test_context_menu(self, browser):
        browser.get(URLs.CONTEXT_MENU_PAGE)
        context_menu_page = ContextMenuPage(browser=browser)
        assert context_menu_page.open(), "Ошибка при попытке открытия страницы с контекстным меню \n"
        assert context_menu_page.check_context_menu(
            text=TestDataContextMenu.TEST_ALERT_TEXT), "Ошибка при попытке проверить контекстное меню \n"
