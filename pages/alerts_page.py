from pages.base_page import BasePage

class AlertsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def process_js_alert(self):
        pass

