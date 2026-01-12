from pages.base_page import BasePage
from utils.random.random_factory import RandomFactory
from elements.custom_elements.label import Label


class AlertsPage(BasePage):
    ALERT_PAGE_UNIQUE_LOC = "//div[contains(@class,'example')]//*[contains(text(), 'JavaScript Alerts')]"
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
                                    locator=self.ALERT_PAGE_UNIQUE_LOC,
                                    description="JavaScript Alerts Page -> JavaScript Alerts label")
        self.random_factory = RandomFactory()

    def get_result_text(self):
        return self.element(locator=self.ALERT_RESULT_TEXT).get_text()

    def get_random_string(self):
        return self.random_factory.get_random_string()

    def click_alert_button(self) -> None:
        self.element(locator=self.ALERT_BUTTON).click()

    def click_confirm_button(self) -> None:
        self.element(locator=self.CONFIRM_BUTTON).click()

    def click_prompt_button(self) -> None:
        self.element(locator=self.PROMPT_BUTTON).click()
