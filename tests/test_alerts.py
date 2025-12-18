from pages.alerts_page import AlertsPage
from pages.js.alerts_js import AlertsJS
from config.urls import URLs


class TestAlerts:

    def test_alerts(self, browser):
        alerts_page = AlertsPage(browser)
        browser.get(URLs.ALERTS_PAGE)
        assert alerts_page.open(), "Ошибка при открытии страницы с алертами \n"
        assert alerts_page.check_alert(), "Ошибка при проверке алерта \n"
        assert alerts_page.check_confirm(), "Ошибка при проверке алерта с подтверждением \n"
        assert alerts_page.check_prompt(), "Ошибка при проверке алерта с полем и отправкой значения \n"

        alerts_js = AlertsJS(browser)
        assert alerts_js.check_alert_js(), "Ошибка при проверке алерта с JavaScript \n"
        assert alerts_js.check_confirm_js(), "Ошибка при проверке алерта с подтверждением с JavaScript \n"
        assert alerts_js.check_prompt_js(), "Ошибка при проверке алерта с полем и отправкой значения с JavaScript \n"
