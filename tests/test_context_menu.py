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
        actual_alert_text = context_menu_page.get_alert_text()
        assert actual_alert_text  == TestDataContextMenu.TEST_ALERT_TEXT, \
            ("Ошибка при проверке текста алерта \n"
             f"Actual: {actual_alert_text} \n"
             f"Expected: {TestDataContextMenu.TEST_ALERT_TEXT}")
        context_menu_page.confirm_alert()
