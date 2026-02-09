from pages.alerts_page import AlertsPage
from data.alerts_data import AlertsData
from config.urls import URLs
import pytest

from utils.markers.markers import critical
from utils.random.random_factory import RandomFactory


@pytest.fixture
def alerts_test_context(browser):
    browser.get(URLs.ALERTS_PAGE)
    alerts_page = AlertsPage(browser)
    alerts_page.wait_for_open()
    yield alerts_page

@critical
class TestAlerts:

    def test_alert_manual(self, browser, alerts_test_context):
        alerts_page = alerts_test_context
        alerts_page.click_alert_button()
        actual_alert_text = browser.get_alert_text()
        assert actual_alert_text == AlertsData.ALERT_TEXT, ("Ошибка при проверке текста алерта \n"
                                                                f"Actual: {actual_alert_text} \n"
                                                                f"Expected: {AlertsData.ALERT_TEXT}")
        browser.confirm_alert()
        actual_result_text = alerts_page.get_result_text()
        assert actual_result_text == AlertsData.ALERT_RESULT_TEXT, \
            ("Ошибка при проверке результата текста алерта \n"
             f"Actual: {actual_result_text} \n"
             f"Expected: {AlertsData.ALERT_RESULT_TEXT}")

    def test_confirm_manual(self, browser, alerts_test_context):
        alerts_page = alerts_test_context
        alerts_page.click_confirm_button()
        actual_alert_text = browser.get_alert_text()
        assert actual_alert_text == AlertsData.CONFIRM_TEXT, \
            ("Ошибка при проверке текста алерта типа Confirm \n"
             f"Actual: {actual_alert_text} \n"
             f"Expected: {AlertsData.CONFIRM_TEXT}")
        browser.confirm_alert()
        actual_result_text = alerts_page.get_result_text()
        assert actual_result_text == AlertsData.CONFIRM_RESULT_TEXT, \
            ("Ошибка при проверке результата алерта типа Confirm \n"
             f"Actual: {actual_result_text} \n"
             f"Expected: {AlertsData.CONFIRM_RESULT_TEXT}")

    def test_prompt_manual(self, browser, alerts_test_context):
        alerts_page = alerts_test_context
        alerts_page.click_prompt_button()
        random_string = RandomFactory.get_random_string(AlertsData.STRING_LENGTH)
        actual_alert_text = browser.get_alert_text()
        assert actual_alert_text == AlertsData.PROMPT_TEXT, \
            ("Ошибка при проверке текста алерта типа Prompt \n"
             f"Actual: {actual_alert_text} \n"
             f"Expected: {AlertsData.PROMPT_TEXT}")
        browser.send_keys_alert(random_string)
        browser.confirm_alert()
        actual_result_text = alerts_page.get_result_text()
        assert actual_result_text == AlertsData.PROMPT_RESULT_TEXT + random_string, \
            ("Ошибка при проверке результата алерта типа Prompt \n"
             f"Actual: {actual_alert_text} \n"
             f"Expected: {AlertsData.PROMPT_RESULT_TEXT + random_string}")

    def test_alert_with_js(self, browser, alerts_test_context):
        alerts_page = alerts_test_context
        alerts_page.click_alert_button_with_js()
        actual_alert_text = browser.get_alert_text()
        assert actual_alert_text == AlertsData.ALERT_TEXT, \
            ("Ошибка при проверке текста алерта \n"
             f"Actual: {actual_alert_text} \n"
             f"Expected: {AlertsData.ALERT_TEXT}")
        browser.confirm_alert()
        actual_result_text = alerts_page.get_result_text_with_js()
        assert actual_result_text == AlertsData.ALERT_RESULT_TEXT, \
            ("Ошибка при проверке результата текста алерта \n"
             f"Actual: {actual_result_text} \n"
             f"Expected: {AlertsData.ALERT_RESULT_TEXT}")

    def test_confirm_with_js(self, browser, alerts_test_context):
        alerts_page = alerts_test_context
        alerts_page.click_confirm_button_with_js()
        actual_alert_text = browser.get_alert_text()
        assert actual_alert_text == AlertsData.CONFIRM_TEXT, \
            ("Ошибка при проверке текста алерта типа Confirm \n"
             f"Actual: {actual_alert_text} \n"
             f"Expected: {AlertsData.CONFIRM_TEXT}")
        browser.confirm_alert()
        actual_result_text = alerts_page.get_result_text_with_js()
        assert actual_result_text == AlertsData.CONFIRM_RESULT_TEXT, \
            ("Ошибка при проверке результата алерта типа Confirm \n"
             f"Actual: {actual_result_text} \n"
             f"Expected: {AlertsData.CONFIRM_RESULT_TEXT}")

    def test_prompt_with_js(self, browser, alerts_test_context):
        alerts_page = alerts_test_context
        alerts_page.click_prompt_button_with_js()
        random_string = RandomFactory.get_random_string(AlertsData.STRING_LENGTH)
        actual_alert_text = browser.get_alert_text()
        assert actual_alert_text == AlertsData.PROMPT_TEXT, \
            ("Ошибка при проверке текста алерта типа Prompt \n"
             f"Actual: {actual_alert_text} \n"
             f"Expected: {AlertsData.PROMPT_TEXT}")
        browser.send_keys_alert(random_string)
        browser.confirm_alert()
        actual_result_text = alerts_page.get_result_text_with_js()
        assert actual_result_text == AlertsData.PROMPT_RESULT_TEXT + random_string, \
            ("Ошибка при проверке результата алерта типа Prompt \n"
             f"Actual: {actual_result_text} \n"
             f"Expected: {AlertsData.PROMPT_RESULT_TEXT + random_string}")
