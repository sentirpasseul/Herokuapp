from enum import StrEnum

from pages.context_menu_page import ContextMenuPage

class TestDataContextMenu(StrEnum):
    TEST_ALERT_TEXT = "You selected a context menu"

class TestContextMenu:

    def test_context_menu(self, browser):
        context_menu_page = ContextMenuPage(browser=browser, text=TestDataContextMenu.TEST_ALERT_TEXT)
        assert context_menu_page.open()
        assert context_menu_page.check_context_menu()

