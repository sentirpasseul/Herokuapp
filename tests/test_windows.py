from pages.windows_page import WindowsPage
from config.urls import URLs
from data.windows_data import TestWindowsData


class TestWindows:

    def test_windows_page(self, browser):
        browser.get(url=URLs.WINDOWS_PAGE)

        windows_page = WindowsPage(browser)

        windows_page.wait_for_open()
        windows_page.click_link()
        windows_page.open_new_tab()
        windows_page.new_window_label.with_text(TestWindowsData.TEXT_NEW_PAGE)
        actual_title = windows_page.get_new_window_title()
        assert actual_title == TestWindowsData.TITLE_NEW_PAGE, ("Ошибка при проверке имени новой вкладки \n"
                                                                f"Actual: {actual_title}\n"
                                                                f"Expected: {TestWindowsData.TITLE_NEW_PAGE}")
