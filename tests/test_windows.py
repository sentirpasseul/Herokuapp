from pages.new_window_page import NewWindowPage
from pages.windows_page import WindowsPage
from config.urls import URLs
from data.windows_data import WindowsData


class TestWindows:

    def test_windows_page(self, browser):
        browser.get(url=URLs.WINDOWS_PAGE)

        windows_page = WindowsPage(browser)
        new_window_page = NewWindowPage(browser)

        windows_page.wait_for_open()
        windows_page.click_link()
        browser.switch_to_new_tab()

        new_window_page.wait_for_open()
        actual_window_title = browser.get_title()
        assert actual_window_title == WindowsData.TITLE_NEW_PAGE, \
            ("Ошибка при проверке имени новой вкладки \n"
             f"Actual: {actual_window_title}\n"
             f"Expected: {WindowsData.TITLE_NEW_PAGE}")
