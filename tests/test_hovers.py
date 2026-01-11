from pages.hovers_page import HoversPage
from config.urls import URLs


class TestHovers:
    def test_hovers_page(self, browser):
        browser.get(URLs.HOVERS_PAGE)
        hovers_page = HoversPage(browser=browser)
        assert hovers_page.wait_for_open(), "Ошибка при открытии страницы c ховерами"
        hovers_page.check_user_cards()
