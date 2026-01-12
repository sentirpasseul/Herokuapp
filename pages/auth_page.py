from pages.base_page import BasePage
from elements.custom_elements.label import Label


class AuthPage(BasePage):
    UNIQUE_LOC = "//*[contains(text(), 'Basic Auth')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Basic Auth Page -> Basic Auth label")
        self.success_message = Label(browser=self.browser,
                                     locator='//p[contains(text(), "Congratulations! You must have the proper credentials.")]',
                                     description="Basic Auth Page -> Success auth message label")

    def wait_for_success_message(self):
        self.success_message.wait_for_visible()

