from pages.infinite_scroll_page import InfiniteScrollPage
from config.urls import URLs
from data.infinite_scroll_data import InfiniteScrollData
from utils.markers.markers import critical


@critical
class TestInfiniteScroll:

    def test_infinite_scroll(self, browser):
        browser.get(URLs.INFINITE_SCROLL_PAGE)
        infinite_scroll_page = InfiniteScrollPage(browser)
        infinite_scroll_page.wait_for_open()

        while infinite_scroll_page.get_paragraphs_count() < InfiniteScrollData.ENGINEER_AGE:
            last_paragraph = infinite_scroll_page.get_paragraphs_count()
            infinite_scroll_page.scroll_to_paragraph_by_index(last_paragraph)
