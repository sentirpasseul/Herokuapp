from pages.upload_image import UploadImagePage
from config.urls import URLs
from data.upload_image_data import UploadImageTestData
import pytest

from utils.path.path_utils import PathUtils


@pytest.fixture
def upload_image_test_context(browser):
    browser.get(URLs.UPLOAD_IMAGE_PAGE)
    upload_image_page = UploadImagePage(browser)
    upload_image_page.wait_for_open()
    yield upload_image_page


class TestUploadImage:

    def test_upload_image(self, upload_image_test_context):
        self.upload_image_page = upload_image_test_context
        self.upload_image_page.wait_for_open()

        assert self.upload_image_page.is_image_loader_visible(), \
            "Ошибка при проверке видимости кнопки загрузки изображения"
        self.upload_image_page.clear_values_to_image_loader()
        self.upload_image_page.upload_image(UploadImageTestData.IMAGE_NAME)
        self.upload_image_page.click_submit_button()
        assert self.upload_image_page.is_file_uploaded_successful_text_visible(), \
            "Ошибка при проверке видимости текста об успешной загрузки файла"
        assert self.upload_image_page.is_uploaded_file_name_visible(), \
            "Ошибка при проверке видимости имени загруженного файла"

    @pytest.mark.skip
    def test_upload_image_with_dialog_window(self, upload_image_test_context):
        from utils.pyautogui.pyautogui_utilities import PyAutoGuiUtilities
        self.upload_image_page = upload_image_test_context
        self.upload_image_page.wait_for_open()

        self.upload_image_page.click_upload_image_area()
        image_path = PathUtils.get_data_path(UploadImageTestData.IMAGE_NAME)
        PyAutoGuiUtilities.upload_file(image_path)
        assert self.upload_image_page.is_uploaded_file_name_in_uploaded_area_visible(), \
            "Ошибка при проверке видимости имени загруженного файла в поле загрузки файлов"
        assert self.upload_image_page.is_mark_text_visible(), \
            'Ошибка при проверке видимости "✔" '
