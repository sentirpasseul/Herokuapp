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
        assert self.alerts_page.alerts.get_alert_text() == TestAlertsData.ALERT_TEXT, "Ошибка при проверке текста алерта"
        self.alerts_page.alerts.accept_alert()
        assert self.alerts_page.get_result_text() == TestAlertsData.ALERT_RESULT_TEXT, \
            "Ошибка при проверке результата текста алерта"

    def test_confirm_manual(self):
        self.alerts_page.click_confirm_button()
        assert self.alerts_page.alerts.get_alert_text() == TestAlertsData.CONFIRM_TEXT, \
            "Ошибка при проверке текста алерта типа Confirm"
        self.alerts_page.alerts.accept_alert()
        assert self.alerts_page.get_result_text() == TestAlertsData.CONFIRM_RESULT_TEXT, \
            "Ошибка при проверке результата алерта типа Confirm"

    def test_prompt_manual(self):
        self.alerts_page.click_prompt_button()
        random_string = self.alerts_page.get_random_string(TestAlertsData.STRING_LENGTH)
        assert self.alerts_page.alerts.get_alert_text() == TestAlertsData.PROMPT_TEXT, \
            "Ошибка при проверке текста алерта типа Prompt"
        self.alerts_page.alerts.send_keys_to_alert(random_string)
        self.alerts_page.alerts.accept_alert()
        assert self.alerts_page.get_result_text() == TestAlertsData.PROMPT_RESULT_TEXT + random_string, \
            "Ошибка при проверке результата алерта типа Prompt"

    def test_alert_with_js(self):
        self.alerts_page.click_alert_button_with_js()
        assert self.alerts_page.alerts.get_alert_text() == TestAlertsData.ALERT_TEXT, "Ошибка при проверке текста алерта"
        self.alerts_page.alerts.accept_alert()
        assert self.alerts_page.get_result_text_with_js() == TestAlertsData.ALERT_RESULT_TEXT, \
            "Ошибка при проверке результата текста алерта"

    def test_confirm_with_js(self):
        self.alerts_page.click_confirm_button_with_js()
        assert self.alerts_page.alerts.get_alert_text() == TestAlertsData.CONFIRM_TEXT, \
            "Ошибка при проверке текста алерта типа Confirm"
        self.alerts_page.alerts.accept_alert()
        assert self.alerts_page.get_result_text_with_js() == TestAlertsData.CONFIRM_RESULT_TEXT, \
            "Ошибка при проверке результата алерта типа Confirm"

    def test_prompt_with_js(self):
        self.alerts_page.click_prompt_button_with_js()
        random_string = self.alerts_page.get_random_string(TestAlertsData.STRING_LENGTH)
        assert self.alerts_page.alerts.get_alert_text() == TestAlertsData.PROMPT_TEXT, \
            "Ошибка при проверке текста алерта типа Prompt"
        self.alerts_page.alerts.send_keys_to_alert(random_string)
        self.alerts_page.alerts.accept_alert()
        assert self.alerts_page.get_result_text_with_js() == TestAlertsData.PROMPT_RESULT_TEXT + random_string, \
            "Ошибка при проверке результата алерта типа Prompt"
