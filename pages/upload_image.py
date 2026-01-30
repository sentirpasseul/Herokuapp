from token import LBRACE

from pages.base_page import BasePage
from elements.custom_elements.label import Label
from elements.custom_elements.input import Input
from elements.custom_elements.web_element import WebElement
from utils.path.path_utils import PathUtils


class UploadImagePage(BasePage):
    UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'File Uploader')]"
    FILE_UPLOADED_SUCCESSFUL_TEXT = "//div[contains(@class, 'example')]//*[contains(text(), 'File Uploaded!')]"
    INPUT_LOC = "file-upload"
    BUTTON_LOC = "file-submit"
    UPLOADED_FILE_NAME = "uploaded-files"
    DRAG_AND_DROP_AREA = "drag-drop-upload"
    MARK_TEXT = "//*[contains(text(),'✔')]"
    UPLOADED_IMAGE_NAME_IN_UPLOADED_AREA = "//div[contains(@class, 'dz-filename')]"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(
            browser=browser,
            locator=self.UNIQUE_LOC,
            description="Upload Image Page -> File Uploader label"
        )
        self.image_loader = Input(browser=self.browser,
                                  locator=self.INPUT_LOC,
                                  description="Upload Image Page -> Loader Image input")
        self.submit_button = WebElement(browser=self.browser,
                                        locator=self.BUTTON_LOC,
                                        description="Upload Image Page -> Loader Image Submit button")
        self.upload_image_area = WebElement(browser=self.browser,
                                            locator=self.DRAG_AND_DROP_AREA,
                                            description="Upload Image Page -> Drag And Drop Area container")
        self.file_uploaded_successful_text = Label(browser=self.browser,
                                                   locator=self.FILE_UPLOADED_SUCCESSFUL_TEXT,
                                                   description=f"Upload Image Page -> File Uploaded Successful label")
        self.mark_text = Label(browser=self.browser,
                               locator=self.MARK_TEXT,
                               description="Upload Image Page -> Mark label")
        self.uploaded_file_name = Label(browser=self.browser,
                                        locator=self.UPLOADED_FILE_NAME,
                                        description="Upload Image Page -> Uploaded File Text label")
        self.uploaded_image_name_in_uploaded_area = Label(browser=self.browser,
                                                          locator=self.UPLOADED_IMAGE_NAME_IN_UPLOADED_AREA,
                                                          description="Upload Image Page -> Uploaded File Name In Uploaded Area label")

    def click_submit_button(self) -> None:
        self.submit_button.click()

    def click_upload_image_area(self) -> None:
        self.upload_image_area.click()

    def upload_image(self, image_name: str) -> None:
        image_path = PathUtils.get_data_path(file_name=image_name)
        self.image_loader.send_keys(image_path)

    def is_image_loader_visible(self) -> bool:
        return self.image_loader.is_exists()

    def clear_values_to_image_loader(self) -> None:
        self.image_loader.clear()

    def is_file_uploaded_successful_text_visible(self) -> bool:
        return self.file_uploaded_successful_text.is_exists()

    def is_uploaded_file_name_visible(self) -> bool:
        return self.uploaded_file_name.is_exists()

    def is_uploaded_file_name_in_uploaded_area_visible(self) -> bool:
        return self.uploaded_image_name_in_uploaded_area.is_exists()

    def is_mark_text_visible(self) -> bool:
        return self.mark_text.is_exists()
