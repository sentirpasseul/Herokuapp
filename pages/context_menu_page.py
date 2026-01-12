from pages.base_page import BasePage
from utils.logs.logger import Logger
from pages.alerts_page import AlertsPage
from selenium.common.exceptions import TimeoutException
from elements.custom_elements.label import Label
from elements.custom_elements.web_element import WebElement


class ContextMenuPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Context Menu')]"
    AREA_CONTEXT_UNIQUE_LOC = "hot-spot"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Context Menu Page - > Context Menu label")
        self.context_area = WebElement(browser=self.browser,
                                  locator=self.AREA_CONTEXT_UNIQUE_LOC,
                                  description="Context Menu Page -> Hot Spot Area container")
        self.alerts = AlertsPage(browser)

    def open_context_menu_in_area(self) -> None:
        self.context_area.open_context_menu()
