from pages.base_page import BasePage
from utils.random.random_factory import RandomFactory
from elements.custom_elements.label import Label
from elements.custom_elements.button import Button


class AlertsPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class,'example')]//*[contains(text(), 'JavaScript Alerts')]"
    ALERT_RESULT_TEXT = "//*[@*='result']"

    ALERT_BUTTON = "//button[@onclick = 'jsAlert()']"
    CONFIRM_BUTTON = "//button[@onclick = 'jsConfirm()']"
    PROMPT_BUTTON = "//button[@onclick = 'jsPrompt()']"

    BUTTON_ALERT_JS = "jsAlert()"
    BUTTON_CONFIRM_JS = "jsConfirm()"
    BUTTON_PROMPT_JS = "jsPrompt()"

    RESULT_TEXT_ID = 'result'

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="JavaScript Alerts Page -> JavaScript Alerts label")
        self.result_text = Label(browser=browser,
                                 locator=self.ALERT_RESULT_TEXT,
                                 description="JavaScript Alerts Page -> Result label")
        self.alert_button = Button(browser=browser,
                                   locator=self.ALERT_BUTTON,
                                   description="JavaScript Alerts Page -> Alert button")
        self.confirm_button = Button(browser=browser,
                                     locator=self.CONFIRM_BUTTON,
                                     description="JavaScript Alerts Page -> Confirm button")
        self.prompt_button = Button(browser=browser,
                                    locator=self.PROMPT_BUTTON,
                                    description="JavaScript Alerts Page -> Prompt button")
        self.random_factory = RandomFactory()

    def get_result_text(self):
        return self.result_text.get_text()

    def get_random_string(self, string_length: int):
        return self.random_factory.get_random_string(string_length)

    def click_alert_button(self) -> None:
        self.alert_button.click()

    def click_confirm_button(self) -> None:
        self.confirm_button.click()

    def click_prompt_button(self) -> None:
        self.prompt_button.click()

    def click_alert_button_with_js(self) -> None:
        self.browser.click_button_with_js(self.BUTTON_ALERT_JS)

    def click_confirm_button_with_js(self) -> None:
        self.browser.click_button_with_js(self.BUTTON_CONFIRM_JS)

    def click_prompt_button_with_js(self) -> None:
        self.browser.click_button_with_js(self.BUTTON_PROMPT_JS)

    def get_result_text_with_js(self):
        return self.browser.get_text_with_js(self.RESULT_TEXT_ID)
