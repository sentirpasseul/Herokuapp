from pages.windows_page import WindowsPage
from config.urls import URLs
from data.windows_data import TestWindowsData
from elements.common.window_handler import WindowHandler


class TestWindows:

    def test_windows_page(self, browser):
        browser.get(url=URLs.WINDOWS_PAGE)

        windows_page = WindowsPage(browser)
        window_handler = WindowHandler(browser)

        windows_page.wait_for_open()
        windows_page.click_link()
        window_handler.open_new_tab()
        windows_page.new_window_label.with_text(TestWindowsData.TEXT_NEW_PAGE)
        assert windows_page.get_new_window_title() == TestWindowsData.TITLE_NEW_PAGE, "Ошибка при проверке имени новой вкладки"
