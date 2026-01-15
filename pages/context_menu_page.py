from pages.base_page import BasePage
from elements.custom_elements.label import Label
from elements.custom_elements.web_element import WebElement


class ContextMenuPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Context Menu')]"
    AREA_CONTEXT_LOC = "hot-spot"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Context Menu Page - > Context Menu label")
        self.context_area = WebElement(browser=self.browser,
                                       locator=self.AREA_CONTEXT_LOC,
                                       description="Context Menu Page -> Hot Spot Area container")

    def open_context_menu_in_area(self) -> None:
        self.context_area.open_context_menu()

    def get_alert_text(self):
        return self.browser.get_alert_text()

    def confirm_alert(self):
        self.browser.confirm_alert()
