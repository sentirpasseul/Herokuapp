from core.browser import Browser


class AlertHandler:

    def __init__(self, browser: Browser):
        self.browser = browser

    def get_alert_text(self):
        return self.browser.get_alert_text()

    def accept_alert(self) -> None:
        self.browser.confirm_alert()

    def send_keys_to_alert(self, value) -> None:
        self.browser.send_keys_alert(value)
