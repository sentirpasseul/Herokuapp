from pages.infinite_scroll_page import InfiniteScrollPage
from config.urls import URLs

class TestInfiniteScrollPage:
    ENGINEER_AGE = 25

    def test_infinite_scroll(self, browser):
        browser.get(URLs.INFINITE_SCROLL_PAGE)
        infinite_scroll_page = InfiniteScrollPage(browser)
        assert infinite_scroll_page.open(), "Ошибка при открытии страницы с бесконечным скролом"
        assert infinite_scroll_page.check_quantity_paragraphs_to_engineer_age(age=self.ENGINEER_AGE), \
            "Ошибка при проверке количества абзацев с возрастом инженера, выполняющим задание"
