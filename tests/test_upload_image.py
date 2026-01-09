from pages.upload_image import UploadImagePage
from config.urls import URLs
from enum import StrEnum


class TestData(StrEnum):
    IMAGE_NAME_PATH = "Rectangle1.png"

class TestUploadImage:
    def test_upload_image(self, browser):
        browser.get(URLs.UPLOAD_IMAGE_PAGE)
        upload_image_page = UploadImagePage(browser)
        assert upload_image_page.open(), "Ошибка при открытии страницы с загрузчиком изображения"
        assert upload_image_page.is_image_uploaded(TestData.IMAGE_NAME_PATH)
        assert upload_image_page.check_upload_image_successful(), "Ошибка при проверке загрузки изображения"

