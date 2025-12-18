from enum import StrEnum

from pages.alerts_page import AlertsPage, TestAlertsData
from utils.logs.logger import Logger


class AlertsJS(AlertsPage):
    BUTTON_ALERT_JS = "jsAlert()"
    BUTTON_CONFIRM_JS = "jsConfirm()"
    BUTTON_PROMPT_JS = "jsPrompt()"

    def check_alert_js_open(self, selector: str):
        try:
            script = f"document.querySelector('[onClick=\"{selector}\"]').click()"
            self.browser.execute_script(script)
            Logger.info(f"Alert open successful")
        except Exception as err:
            Logger.error(f"Failed to open alert: {err}")

    def check_result_text_js(self, text):
        try:
            script = f"document.getElementById('result').textContent"
            self.check_result_text(self.browser.execute_script(script))
            return True
        except Exception as err:
            Logger.error(f"Failed to check '{text}': {err}")
            return False

    def check_alert_js(self):
        try:
            self.check_alert_js_open(self.BUTTON_ALERT_JS)
            self.check_alert_text(TestAlertsData.ALERT_TEXT)
            self.browser.confirm_alert()
            self.check_result_text_js(TestAlertsData.ALERT_RESULT_TEXT)
            Logger.info(f"Check alert using JavaScript is successful")
            return True
        except Exception as err:
            Logger.error(f"Failed to check alert using JavaScript: {err}")
            return False

    def check_confirm_js(self):
        try:
            self.check_alert_js_open(self.BUTTON_CONFIRM_JS)
            self.check_alert_text(TestAlertsData.CONFIRM_TEXT)
            self.browser.confirm_alert()
            self.check_result_text_js(TestAlertsData.CONFIRM_RESULT_TEXT)
            Logger.info(f"Check confirm using JavaScript is successful")
            return True
        except Exception as err:
            Logger.error(f"Failed to check confirm using JavaScript: {err}")
            return False

    def check_prompt_js(self):
        try:
            self.check_alert_js_open(self.BUTTON_PROMPT_JS)
            self.check_alert_text(TestAlertsData.PROMPT_TEXT)
            random_string = self.get_random_string()
            self.browser.send_keys_alert(random_string)
            self.browser.confirm_alert()
            self.check_result_text_js(TestAlertsData.PROMPT_RESULT_TEXT + random_string)
            Logger.info(f"Check prompt using JavaScript is successful")
            return True
        except Exception as err:
            Logger.error(f"Failed to check prompt using JavaScript: {err}")
            return False
