from pages.base_page import BasePage
from elements.custom_elements.label import Label


class AuthPage(BasePage):
    UNIQUE_LOC = "//*[contains(text(), 'Basic Auth')]"
    SUCCESS_MESSAGE = "//div[contains(@class, 'example')]//*[contains(text(), 'Congratulations!')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Basic Auth Page -> Basic Auth label")
        self.success_message = Label(browser=self.browser,
                                     locator=self.SUCCESS_MESSAGE,
                                     description="Basic Auth Page -> Success auth message label")

    def is_success_message_exists(self):
        return self.success_message.is_exists()
