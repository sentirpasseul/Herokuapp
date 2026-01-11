from pages.dynamic_content_page import DynamicContentPage
from config.urls import URLs


class TestDynamicContentPage:
    def test_dynamic_content_page(self, browser):
        browser.get(URLs.DYNAMIC_CONTENT_PAGE)
        dynamic_content_page = DynamicContentPage(browser)
        assert dynamic_content_page.wait_for_open(), "Ошибка при открытии страницы с динамическим контентом"
        assert dynamic_content_page.check_images_two_coincidence(), "Ошибка при проверке на соответствие 2 одинаковых изображений"
