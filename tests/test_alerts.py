from pages.alerts_page import AlertsPage
from pages.js.alerts_js import AlertsJS


class TestAlerts:

    def test_alerts(self, browser):
        alerts_page = AlertsPage(browser)
        assert alerts_page.open()
        assert alerts_page.check_alert()
        assert alerts_page.check_confirm()
        assert alerts_page.check_prompt()

        alerts_js = AlertsJS(browser)
        assert alerts_js.check_alert_js()
        assert alerts_js.check_confirm_js()
        assert alerts_js.check_prompt_js()
