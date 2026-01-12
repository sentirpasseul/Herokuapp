from core.browser import Browser
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from elements.custom_elements.label import Label


class WindowsPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Opening a new window')]"
    NEW_WINDOW_LINK = "//a[contains(@href, '/windows/new')]"
    NEW_WINDOW_TAB_LABEL = "//div[contains(@class, 'example')]//*[contains(text(), '{text}')]"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Windows Page -> Windows page label")
        self.new_window_label = Label(browser=self.browser,
                                     locator=self.NEW_WINDOW_TAB_LABEL.format(text=label),
                                     description="Windows Page -> New window page label")
        self.link = Label(browser=self.browser,
                         locator=self.NEW_WINDOW_LINK,
                         description="Windows Page -> New window link")


    def check_open_new_tab(self, label: str, title: str):
        try:
            self.browser.switch_to_new_tab()

            new_window_label.wait_for_visible()
            new_window_title = self.browser.get_title()
            return True if new_window_title == title else False
        except TimeoutException:
            return False

    def check_link(self):
        try:

            link.wait_for_visible()
            link.click()
            return True
        except TimeoutException:
            return False

    def check_return_to_original_page(self):
        try:
            self.browser.switch_to_original_window()
            self.open()
            return True
        except TimeoutException:
            return False

    def check_close_tabs(self):
        try:
            handles = self.browser.driver.window_handles
            if len(handles) <= 1:
                return True

            for handle in handles[1:]:
                self.browser.switch_to_window(handle)
                self.browser.close()

            self.browser.switch_to_original_window()
            return True
        except TimeoutException:
            return False
