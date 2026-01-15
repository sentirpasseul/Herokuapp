from pages.infinite_scroll_page import InfiniteScrollPage
from config.urls import URLs
from data.infinite_scroll_data import InfiniteScrollData


class TestInfiniteScroll:

    def test_infinite_scroll(self, browser):
        browser.get(URLs.INFINITE_SCROLL_PAGE)
        infinite_scroll_page = InfiniteScrollPage(browser)
        age = InfiniteScrollData.ENGINEER_AGE

        infinite_scroll_page.wait_for_open()

        current_count_paragraphs = len(infinite_scroll_page.get_paragraphs())
        while current_count_paragraphs < age:
            paragraphs = infinite_scroll_page.get_paragraphs()
            current_count_paragraphs = len(paragraphs)

            if current_count_paragraphs >= age:
                break

            last_paragraph = paragraphs[-1]
            last_paragraph.is_displayed()
            last_paragraph.scroll_to_element(block='end')
