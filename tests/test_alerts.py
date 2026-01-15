from pages.alerts_page import AlertsPage
from data.alerts_data import TestAlertsData
from config.urls import URLs
import pytest


class TestAlerts:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        browser.get(URLs.ALERTS_PAGE)
        self.alerts_page = AlertsPage(browser)
        self.alerts_page.wait_for_open()

    def test_alert_manual(self):
        self.alerts_page.click_alert_button()
        actual_alert_text = self.alerts_page.get_alert_text()
        assert actual_alert_text == TestAlertsData.ALERT_TEXT, ("Ошибка при проверке текста алерта \n"
                                                                f"Actual: {actual_alert_text} \n"
                                                                f"Expected: {TestAlertsData.ALERT_TEXT}")
        self.alerts_page.confirm_alert()
        actual_result_text = self.alerts_page.get_result_text()
        assert actual_result_text == TestAlertsData.ALERT_RESULT_TEXT, \
            ("Ошибка при проверке результата текста алерта \n"
             f"Actual: {actual_result_text} \n"
             f"Expected: {TestAlertsData.ALERT_RESULT_TEXT}")

    def test_confirm_manual(self):
        self.alerts_page.click_confirm_button()
        actual_alert_text = self.alerts_page.get_alert_text()
        assert actual_alert_text == TestAlertsData.CONFIRM_TEXT, \
            ("Ошибка при проверке текста алерта типа Confirm \n"
             f"Actual: {actual_alert_text} \n"
             f"Expected: {TestAlertsData.CONFIRM_TEXT}")
        self.alerts_page.confirm_alert()
        actual_result_text = self.alerts_page.get_result_text()
        assert actual_result_text == TestAlertsData.CONFIRM_RESULT_TEXT, \
            ("Ошибка при проверке результата алерта типа Confirm \n"
             f"Actual: {actual_result_text} \n"
             f"Expected: {TestAlertsData.CONFIRM_RESULT_TEXT}")

    def test_prompt_manual(self):
        self.alerts_page.click_prompt_button()
        random_string = self.alerts_page.get_random_string(TestAlertsData.STRING_LENGTH)
        actual_alert_text = self.alerts_page.get_alert_text()
        assert actual_alert_text == TestAlertsData.PROMPT_TEXT, \
            ("Ошибка при проверке текста алерта типа Prompt \n"
             f"Actual: {actual_alert_text} \n"
             f"Expected: {TestAlertsData.PROMPT_TEXT}")
        self.alerts_page.send_keys_to_alert(random_string)
        self.alerts_page.confirm_alert()
        actual_result_text = self.alerts_page.get_result_text()
        assert actual_result_text == TestAlertsData.PROMPT_RESULT_TEXT + random_string, \
            ("Ошибка при проверке результата алерта типа Prompt \n"
             f"Actual: {actual_alert_text} \n"
             f"Expected: {TestAlertsData.PROMPT_RESULT_TEXT + random_string}")

    def test_alert_with_js(self):
        self.alerts_page.click_alert_button_with_js()
        actual_alert_text = self.alerts_page.get_alert_text()
        assert actual_alert_text == TestAlertsData.ALERT_TEXT, \
            ("Ошибка при проверке текста алерта \n"
             f"Actual: {actual_alert_text} \n"
             f"Expected: {TestAlertsData.ALERT_TEXT}")
        self.alerts_page.confirm_alert()
        actual_result_text = self.alerts_page.get_result_text_with_js()
        assert actual_result_text == TestAlertsData.ALERT_RESULT_TEXT, \
            ("Ошибка при проверке результата текста алерта \n"
             f"Actual: {actual_result_text} \n"
             f"Expected: {TestAlertsData.ALERT_RESULT_TEXT}")

    def test_confirm_with_js(self):
        self.alerts_page.click_confirm_button_with_js()
        actual_alert_text = self.alerts_page.get_alert_text()
        assert actual_alert_text == TestAlertsData.CONFIRM_TEXT, \
            ("Ошибка при проверке текста алерта типа Confirm \n"
             f"Actual: {actual_alert_text} \n"
             f"Expected: {TestAlertsData.CONFIRM_TEXT}")
        self.alerts_page.confirm_alert()
        actual_result_text = self.alerts_page.get_result_text_with_js()
        assert actual_result_text == TestAlertsData.CONFIRM_RESULT_TEXT, \
            ("Ошибка при проверке результата алерта типа Confirm \n"
             f"Actual: {actual_result_text} \n"
             f"Expected: {TestAlertsData.CONFIRM_RESULT_TEXT}")

    def test_prompt_with_js(self):
        self.alerts_page.click_prompt_button_with_js()
        random_string = self.alerts_page.get_random_string(TestAlertsData.STRING_LENGTH)
        actual_alert_text = self.alerts_page.get_alert_text()
        assert actual_alert_text == TestAlertsData.PROMPT_TEXT, \
            ("Ошибка при проверке текста алерта типа Prompt \n"
             f"Actual: {actual_alert_text} \n"
             f"Expected: {TestAlertsData.PROMPT_TEXT}")
        self.alerts_page.send_keys_to_alert(random_string)
        self.alerts_page.confirm_alert()
        actual_result_text = self.alerts_page.get_result_text_with_js()
        assert actual_result_text == TestAlertsData.PROMPT_RESULT_TEXT + random_string, \
            ("Ошибка при проверке результата алерта типа Prompt \n"
             f"Actual: {actual_result_text} \n"
             f"Expected: {TestAlertsData.PROMPT_RESULT_TEXT + random_string}")
