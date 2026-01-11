from pages.upload_image import UploadImagePage
from config.urls import URLs
from enum import StrEnum


class TestData(StrEnum):
    IMAGE_NAME_PATH = "Rectangle1.png"


class TestUploadImage:

    def test_upload_image_page_open(self):
        assert self.upload_image_page.wait_for_open(), "Ошибка при открытии страницы с загрузчиком изображения"

    def test_upload_image(self, browser):
        browser.get(URLs.UPLOAD_IMAGE_PAGE)

        self.upload_image_page = UploadImagePage(browser)
        self.test_upload_image_page_open()
        assert self.upload_image_page.is_image_uploaded(TestData.IMAGE_NAME_PATH)
        assert self.upload_image_page.check_upload_image_successful(), "Ошибка при проверке загрузки изображения"

    def test_upload_image_with_dialog_window(self, browser):
        browser.get(URLs.UPLOAD_IMAGE_PAGE)

        self.upload_image_page = UploadImagePage(browser)
        self.test_upload_image_page_open()
        assert self.upload_image_page.check_image_in_drag_and_drop_area(TestData.IMAGE_NAME_PATH), \
            "Ошибка при проверке drag&drop поля"
