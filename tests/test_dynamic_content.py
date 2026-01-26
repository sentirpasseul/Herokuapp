from pages.dynamic_content_page import DynamicContentPage
from config.urls import URLs
from data.dynamic_content_data import DynamicContentData
from utils.logs.logger import Logger


class TestDynamicContent:
    def test_dynamic_content_page(self, browser):
        browser.get(URLs.DYNAMIC_CONTENT_PAGE)
        dynamic_content_page = DynamicContentPage(browser)

        dynamic_content_page.wait_for_open()
        found_images = set()
        found_duplicates = False
        for attempt in range(DynamicContentData.MAX_ATTEMPTS):
            images = dynamic_content_page.get_all_src()

            for image in images:
                if image in found_images:
                    found_duplicates = True
                    break
                found_images.add(image)

            if found_duplicates:
                break

            browser.refresh()
        else:
            raise AssertionError(f"Failed to check dynamic content: {DynamicContentData.MAX_ATTEMPTS} attempts were exceeded")
