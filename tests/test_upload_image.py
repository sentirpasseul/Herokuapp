from pages.upload_image import UploadImagePage
from config.urls import URLs
from data.upload_image_data import UploadImageTestData
import pytest


class TestUploadImage:

    def test_upload_image(self, browser):
        browser.get(URLs.UPLOAD_IMAGE_PAGE)
        self.upload_image_page = UploadImagePage(browser)
        self.upload_image_page.wait_for_open()

        assert self.upload_image_page.is_image_loader_visible(), \
            "Ошибка при проверке видимости кнопки загрузки изображения"
        self.upload_image_page.image_loader_clear_values()
        self.upload_image_page.upload_image(UploadImageTestData.IMAGE_NAME_PATH)
        self.upload_image_page.click_submit_button()
        assert self.upload_image_page.is_file_uploaded_successful_text_visible(), \
            "Ошибка при проверке видимости текста об успешной загрузки файла"
        assert self.upload_image_page.is_uploaded_file_name_visible(), \
            "Ошибка при проверке видимости имени загруженного файла"

    def test_upload_image_with_dialog_window(self, browser):
        browser.get(URLs.UPLOAD_IMAGE_PAGE)
        self.upload_image_page = UploadImagePage(browser)
        self.upload_image_page.wait_for_open()

        self.upload_image_page.click_upload_image_area()
        self.upload_image_page.upload_image_with_finder(UploadImageTestData.IMAGE_NAME_PATH)
        assert self.upload_image_page.is_uploaded_file_name_in_uploaded_area_visible(), \
            "Ошибка при проверке видимости имени загруженного файла в поле загрузки файлов"
        assert self.upload_image_page.is_mark_text_visible(), \
            'Ошибка при проверке видимости "✔" '
