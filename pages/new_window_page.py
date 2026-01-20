from elements.custom_elements.label import Label
from pages.base_page import BasePage


class NewWindowPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'New Window')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="New Window -> New Window label")
