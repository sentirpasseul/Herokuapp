from enum import StrEnum
from config.urls import URLs

from pages.context_menu_page import ContextMenuPage


class TestDataContextMenu(StrEnum):
    TEST_ALERT_TEXT = "You selected a context menu"


class TestContextMenu:

    def test_context_menu(self, browser):
        browser.get(URLs.CONTEXT_MENU_PAGE)
        context_menu_page = ContextMenuPage(browser=browser)
        context_menu_page.wait_for_open()
        context_menu_page.open_context_menu_in_area()
        assert context_menu_page.alerts.get_alert_text() == TestDataContextMenu.TEST_ALERT_TEXT, "Ошибка при проверке текста алерта"
        context_menu_page.alerts.accept_alert()
