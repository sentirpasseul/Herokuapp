from pages.alerts_page import AlertsPage
from config.urls import URLs
from enum import StrEnum
import pytest


class TestAlertsData(StrEnum):
    ALERT_TEXT = "I am a JS Alert"
    ALERT_RESULT_TEXT = "You successfully clicked an alert"

    CONFIRM_TEXT = "I am a JS Confirm"
    CONFIRM_RESULT_TEXT = "You clicked: Ok"

    PROMPT_TEXT = "I am a JS prompt"
    PROMPT_RESULT_TEXT = "You entered: "


class TestAlerts:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        browser.get(URLs.ALERTS_PAGE)
        self.alerts_page = AlertsPage(browser)
        self.alerts_page.wait_for_open()

    def test_alert_manual(self, browser):
        self.alerts_page.click_alert_button()
        browser.switch_to_alert()
        assert browser.get_alert_text() == TestAlertsData.ALERT_TEXT, "Ошибка при проверке текста алерта \n"
        browser.confirm_alert()
        assert self.alerts_page.get_result_text() == TestAlertsData.ALERT_RESULT_TEXT, \
            "Ошибка при проверке результата текста алерта"

    def test_confirm_manual(self, browser):
        self.alerts_page.click_confirm_button()
        browser.switch_to_alert()
        assert browser.get_alert_text() == TestAlertsData.CONFIRM_TEXT, \
            "Ошибка при проверке текста алерта типа Confirm"
        browser.confirm_alert()
        assert self.alerts_page.get_result_text() == TestAlertsData.CONFIRM_RESULT_TEXT, \
            "Ошибка при проверке результата алерта типа Confirm"

    def test_prompt_manual(self, browser):
        self.alerts_page.click_prompt_button()
        browser.switch_to_alert()
        random_string = self.alerts_page.get_random_string()
        assert browser.get_alert_text() == TestAlertsData.PROMPT_TEXT, \
            "Ошибка при проверке текста алерта типа Prompt"
        browser.send_keys_alert(random_string)
        browser.confirm_alert()
        assert self.alerts_page.get_result_text() == TestAlertsData.PROMPT_RESULT_TEXT + random_string, \
            "Ошибка при проверке результата алерта типа Prompt"

    def test_alert_with_js(self, browser):
        browser.click_button_with_js(self.alerts_page.BUTTON_ALERT_JS)
        browser.switch_to_alert()
        assert browser.get_alert_text() == TestAlertsData.ALERT_TEXT, "Ошибка при проверке текста алерта \n"
        browser.confirm_alert()
        assert browser.get_text_with_js(self.alerts_page.RESULT_TEXT_ID) == TestAlertsData.ALERT_RESULT_TEXT, \
            "Ошибка при проверке результата текста алерта"

    def test_confirm_with_js(self, browser):
        browser.click_button_with_js(self.alerts_page.BUTTON_CONFIRM_JS)
        browser.switch_to_alert()
        assert browser.get_alert_text() == TestAlertsData.CONFIRM_TEXT, \
            "Ошибка при проверке текста алерта типа Confirm"
        browser.confirm_alert()
        assert browser.get_text_with_js(self.alerts_page.RESULT_TEXT_ID) == TestAlertsData.CONFIRM_RESULT_TEXT, \
            "Ошибка при проверке результата алерта типа Confirm"

    def test_prompt_with_js(self, browser):
        browser.click_button_with_js(self.alerts_page.BUTTON_PROMPT_JS)
        browser.switch_to_alert()
        random_string = self.alerts_page.get_random_string()
        assert browser.get_alert_text() == TestAlertsData.PROMPT_TEXT, \
            "Ошибка при проверке текста алерта типа Prompt"
        browser.send_keys_alert(random_string)
        browser.confirm_alert()
        assert browser.get_text_with_js(self.alerts_page.RESULT_TEXT_ID) == TestAlertsData.PROMPT_RESULT_TEXT + random_string, \
            "Ошибка при проверке результата алерта типа Prompt"
