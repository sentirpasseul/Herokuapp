from pages.alerts_page import AlertsPage
from pages.js.alerts_js import AlertsJS
from config.urls import URLs
from enum import StrEnum


class TestAlertsData(StrEnum):
    ALERT_TEXT = "I am a JS Alert"
    ALERT_RESULT_TEXT = "You successfully clicked an alert"

    CONFIRM_TEXT = "I am a JS Confirm"
    CONFIRM_RESULT_TEXT = "You clicked: Ok"

    PROMPT_TEXT = "I am a JS prompt"
    PROMPT_RESULT_TEXT = "You entered: "


class TestAlerts:

    def test_alerts(self, browser):
        alerts_page = AlertsPage(browser)
        browser.get(URLs.ALERTS_PAGE)
        assert alerts_page.wait_for_open(), "Ошибка при открытии страницы с алертами \n"

        alerts_page.click_js_alert_button()
        assert browser.get_alert_text() == TestAlertsData.ALERT_TEXT, "Ошибка при проверке текста алерта \n"
        self.browser.confirm_alert()
        assert browser.get == TestAlertsData.ALERT_RESULT_TEXT, "Ошибка при проверке результата текста алерта"

        alerts_page.click_js_confirm_button()
        self.browser.switch_to_alert()
        assert browser.get_alert_text() == TestAlertsData.CONFIRM_TEXT, "Ошибка при проверке текста алерта типа Confirm"
        self.browser.confirm_alert()
        assert alerts_page.get_result_text() == TestAlertsData.CONFIRM_RESULT_TEXT, "Ошибка при проверке результата алерта типа Confirm"

        alerts_page.click_js_prompt_button()
        self.browser.switch_to_alert()
        random_string = alerts_page.get_random_string()
        assert browser.get_alert_text() == TestAlertsData.PROMPT_TEXT, "Ошибка при проверке текста алерта типа Prompt"
        self.browser.send_keys_alert(random_string)
        self.browser.confirm_alert()
        assert alerts_page.get_result_text() == TestAlertsData.PROMPT_RESULT_TEXT, "Ошибка при проверке результата алерта типа Prompt"
