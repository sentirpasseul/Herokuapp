import pytest

from pages.windows_page import WindowsPage
from config.urls import URLs
from data.windows_data import TestWindowsData


class TestWindows:

    def test_windows_page(self, browser):
        browser.get(url=URLs.WINDOWS_PAGE)

        windows_page = WindowsPage(browser)

        windows_page.wait_for_open()
        windows_page.click_link()
        browser.switch_to_new_tab()
        actual_new_window_text = windows_page.get_new_window_text()
        assert actual_new_window_text == TestWindowsData.TEXT_NEW_PAGE, ("Ошибка при проверке текста новой страницы \n"
                                                                         f"Actual: {actual_new_window_text} \n"
                                                                         f"Expected: {TestWindowsData.TEXT_NEW_PAGE}")
        actual_window_title = browser.get_title()
        assert actual_window_title == TestWindowsData.TITLE_NEW_PAGE, ("Ошибка при проверке имени новой вкладки \n"
                                                                f"Actual: {actual_window_title}\n"
                                                                f"Expected: {TestWindowsData.TITLE_NEW_PAGE}")
