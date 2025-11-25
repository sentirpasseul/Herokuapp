from enum import StrEnum

from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from utils.logs.logger import Logger
from utils.random.random_factory import RandomFactory


class AlertsData(StrEnum):
    ALERT_PAGE_LINK = "https://the-internet.herokuapp.com/javascript_alerts"

    ALERT_TEXT = "I am a JS Alert"
    RESULT_ALERT_TEXT = "You successfully clicked an alert"

    CONFIRM_TEXT = "I am a JS Confirm"
    CONFIRM_RESULT_TEXT = "You clicked: Ok"

    PROMPT_TEXT = "I am a JS prompt"
    PROMPT_RESULT_TEXT = "You entered: "


class AlertsPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.unique_element = self.element(locator="//div[contains(@class, "
                                                   "'example')]//*[contains(text(), 'JavaScript Alerts')]",
                                           browser=browser)
        self.random_factory = RandomFactory()

    def open(self):
        try:
            self.browser.get(AlertsData.ALERT_PAGE_LINK)
            self.wait_for_open()
            return True
        except Exception:
            return False

    def get_result_element_text(self):
        return self.element(locator="//*[@*='result']", browser=self.browser).get_text()

    def get_random_string(self):
        return self.random_factory.get_random_string()

    def click_js_alert_button(self) -> None:
        self.element(locator="//button[@onclick = 'jsAlert()']", browser=self.browser).click()

    def click_js_confirm_button(self) -> None:
        self.element(locator="//button[@onclick = 'jsConfirm()']", browser=self.browser).click()

    def click_js_prompt_button(self) -> None:
        self.element(locator="//button[@onclick = 'jsPrompt()']", browser=self.browser).click()

    def check_alert_text(self, text: str):
        correct_text = self.browser.get_alert_text()
        try:
            if text == correct_text:
                Logger.info(f"Alert '{text}' is correct for '{correct_text}'")
                return True
        except Exception as err:
            Logger.error(f"Alert '{text}' is incorrect for '{correct_text}': {err}")
            return False

    def check_result_text(self, text):
        correct_text = self.get_result_element_text()
        try:
            if text == correct_text:
                Logger.info(f"Result '{text}' is correct for {correct_text}")
                return True
        except Exception as err:
            Logger.error(f"Result '{text}' is incorrect for '{correct_text}': {err}")

    def check_alert(self):
        try:
            self.click_js_alert_button()
            self.browser.switch_to_alert()
            if self.check_alert_text(AlertsData.ALERT_TEXT):
                self.browser.confirm_alert()
                if self.check_result_text(AlertsData.RESULT_ALERT_TEXT):
                    Logger.info(f"Check JavaScript alert successful: '{self.get_result_element_text()}' == '{AlertsData.RESULT_ALERT_TEXT}'")
                    return True
        except Exception as err:
            Logger.error(f"Check JavaScript alert failed: {err}")
            return False

    def check_confirm(self):
        try:
            self.click_js_confirm_button()
            self.browser.switch_to_alert()
            if self.check_alert_text(AlertsData.CONFIRM_TEXT):
                self.browser.confirm_alert()
                if self.check_result_text(AlertsData.CONFIRM_RESULT_TEXT):
                    Logger.info(f"Check JavaScript confirm successful: '{self.get_result_element_text()}' == '{AlertsData.CONFIRM_RESULT_TEXT}'")
                    return True
        except Exception as err:
            Logger.error(f"Check JavaScript confirm failed: {err}")
            return False

    def check_prompt(self):
        try:
            self.click_js_prompt_button()
            self.browser.switch_to_alert()
            random_string = self.get_random_string()
            if self.check_alert_text(AlertsData.PROMPT_TEXT):
                self.browser.send_keys(random_string)
                self.browser.confirm_alert()
                if self.check_result_text(AlertsData.PROMPT_RESULT_TEXT + random_string):
                    Logger.info(f"Check JavaScript prompt successful: '{self.get_result_element_text()}'"
                                f" == '{(AlertsData.PROMPT_RESULT_TEXT + random_string)}'")
                    return True
        except Exception as err:
            Logger.error(f"Check JavaScript prompt failed: {err}")
            return False

    def check_alert_js_open(self):
        try:
            script = "document.querySelector('[onClick=\"jsAlert()\"]').click()"
            self.browser.execute_script(script)
            Logger.info(f"Alert open successful")
        except Exception as err:
            Logger.error(f"Failed to open alert: {err}")

    def check_alert_using_js(self):
        script = "document.querySelector('[onClick=\"jsAlert()\"]').click()"
        self.browser.execute_script(script)


