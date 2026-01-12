from pages.base_page import BasePage
from utils.logs.logger import Logger
from pages.alerts_page import AlertsPage
from selenium.common.exceptions import TimeoutException
from elements.custom_elements.label import Label
from elements.custom_elements.container import Container


class ContextMenuPage(BasePage):
    CONTEXT_AREA_LOC = "hot-spot"
    CONTEXT_MENU_PAGE_UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Context Menu')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.CONTEXT_MENU_PAGE_UNIQUE_LOC,
                                    description="Context Menu Page - > Context Menu label")
        self.alerts = AlertsPage(browser)

    def open_context_menu_in_area(self) -> None:
        context_area = Container(browser=self.browser,
                                 locator=self.CONTEXT_AREA_LOC,
                                 description="Context Menu Page -> Hot Spot Area container")
        context_area.open_context_menu()
