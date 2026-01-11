from core.browser import Browser


class AlertsJS():
    BUTTON_ALERT_JS = "jsAlert()"
    BUTTON_CONFIRM_JS = "jsConfirm()"
    BUTTON_PROMPT_JS = "jsPrompt()"

    def __init__(self, browser: Browser):
        self.browser = browser

    def click_button_with_js(self, selector: str) -> None:
        script = f"document.querySelector('[onClick=\"{selector}\"]').click()"
        self.browser.execute_script(script)

    def get_result_text_with_js(self):
        script = f"document.getElementById('result').textContent"
        return self.browser.execute_script(script)
