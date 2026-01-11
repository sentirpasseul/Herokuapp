from enum import StrEnum

from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from utils.logs.logger import Logger
from utils.random.random_factory import RandomFactory
from elements.custom_elements.label import Label


class AlertsPage(BasePage):
    ALERT_PAGE_UNIQUE_LOC = "//div[contains(@class,'example')]//*[contains(text(), 'JavaScript Alerts')]"
    ALERT_RESULT_TEXT = "//*[@*='result']"

    JS_ALERT_BUTTON = "//button[@onclick = 'jsAlert()']"
    JS_CONFIRM_BUTTON = "//button[@onclick = 'jsConfirm()']"
    JS_PROMPT_BUTTON = "//button[@onclick = 'jsPrompt()']"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.ALERT_PAGE_UNIQUE_LOC,
                                    description="JavaScript Alerts Page -> JavaScript Alerts label")
        self.random_factory = RandomFactory()

    def open(self):
        try:
            self.wait_for_open()
            return True
        except TimeoutException:
            return False

    def get_result_text(self):
        return self.element(locator=self.ALERT_RESULT_TEXT).get_text()

    def get_random_string(self):
        return self.random_factory.get_random_string()

    def click_js_alert_button(self) -> None:
        self.element(locator=self.JS_ALERT_BUTTON).click()

    def click_js_confirm_button(self) -> None:
        self.element(locator=self.JS_CONFIRM_BUTTON).click()

    def click_js_prompt_button(self) -> None:
        self.element(locator=self.JS_PROMPT_BUTTON).click()
