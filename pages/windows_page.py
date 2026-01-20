from core.browser import Browser
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from elements.custom_elements.label import Label


class WindowsPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Opening a new window')]"
    NEW_WINDOW_LINK = "//a[contains(@href, '/windows/new')]"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Windows Page -> Windows page label")
        self.link = Label(browser=self.browser,
                          locator=self.NEW_WINDOW_LINK,
                          description="Windows Page -> New window link")

    def click_link(self) -> None:
        self.link.click()
