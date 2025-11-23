from pages.alerts_page import AlertsPage


class TestAlerts:

    def test_alerts(self, browser):
        alerts_page = AlertsPage(browser)
        assert alerts_page.open()
        assert alerts_page.check_js_alert()
        assert alerts_page.check_js_confirm()
        assert alerts_page.check_js_prompt()
