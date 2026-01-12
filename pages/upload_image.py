from token import LBRACE

from pages.base_page import BasePage
from elements.custom_elements.label import Label
from elements.custom_elements.input import Input
from elements.custom_elements.web_element import WebElement
from selenium.common.exceptions import TimeoutException
from utils.pyautogui.pyautogui_utilities import PyAutoGuiUtilities
import os


class UploadImagePage(BasePage):
    UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), '{name}')]"
    INPUT_LOC = "file-upload"
    BUTTON_LOC = "file-submit"
    UPLOADED_FILE_TEXT = "uploaded-files"
    DRAG_AND_DROP_AREA = "drag-drop-upload"
    UPLOADED_IMAGE_TEXT = "//div[contains(@class, 'dz-filename')]"
    MARK_TEXT = "//*[contains(text(),'✔')]"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(
            browser=browser,
            locator=self.UNIQUE_LOC.format(name="File Uploader"),
            description="Upload Image Page -> File Uploader label"
        )
        self.image_loader = Input(browser=self.browser,
                                  locator=self.INPUT_LOC,
                                  description="Upload Image Page -> Loader Image input")
        self.image_name = None
        self.image_path = None
        self.pyautogui = PyAutoGuiUtilities()
        self.name = Label(browser=self.browser,
                          locator=self.UPLOADED_FILE_TEXT,
                          description="Upload Image Page -> Uploaded File label")
        self.submit_button = WebElement(browser=self.browser,
                                        locator=self.BUTTON_LOC,
                                        description="Upload Image Page -> Loader Image Submit button")
        self.area = WebElement(browser=self.browser,
                               locator=self.DRAG_AND_DROP_AREA,
                               description="Upload Image Page -> Drag And Drop Area container")
        self.uploaded_image_text = Label(browser=self.browser,
                                         locator=self.UPLOADED_IMAGE_TEXT,
                                         description=f"Upload Image Page -> Uploaded Image Name label")
        self.mark_text = Label(browser=self.browser,
                               locator=self.MARK_TEXT,
                               description="Upload Image Page -> Mark label")

    @staticmethod
    def get_path_of_image(image_name: str):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "..", "utils", "test_data", image_name)
        final_path = os.path.abspath(file_path)
        return final_path

    def is_image_uploaded(self, image_name_path: str):
        self.image_loader.wait_for_visible()
        self.image_loader.clear()
        image_path = self.get_path_of_image(image_name_path)
        self.image_loader.send_keys(image_path)
        self.image_name = image_name_path

    def check_name_image(self):
        self.name.wait_for_visible()
        return True if self.name == self.image_name else False

    def check_upload_image_successful(self):
        submit_button.click()
        self.unique_element = Label(
            browser=self.browser,
            locator=self.UNIQUE_LOC.format(name="File Uploaded"),
            description="Upload Image Page -> File Uploader label"
        )
        self.open()
        self.check_name_image()

    def check_image_in_drag_and_drop_area(self, image_name: str):
        image_path = self.get_path_of_image(image_name)

        area.click()
        self.pyautogui.upload_file(image_path)

        uploaded_image_text.wait_for_visible()

        mark_text.wait_for_visible()
