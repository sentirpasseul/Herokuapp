from pages.base_page import BasePage
from pages.nested_frames_page import NestedFramesPage
from selenium.common.exceptions import TimeoutException
from elements.custom_elements.label import Label
from elements.custom_elements.web_element import WebElement


class FramePage(BasePage):
    UNIQUE_LOC = "//*[@id='framesWrapper']//*[contains(text(), 'Frames')]"
    MENU_ELEMENT_ITEM = ("//div[contains(@class,'element-list') and contains(@class, 'collapse') and "
                         "contains(@class, 'show')]"
                         "//*[contains(text(), 'Browser Windows')]")
    MENU = "//*[contains(text(),'Browser Windows')]/ancestor::div[contains(@class,'element-group')]//span[contains(@class,'group-header')]"
    MENU_ITEM = "//div[contains(@class,'element-group')]//*[contains(text(), 'Nested Frames')]"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Frames Page -> Frames Page Label")
        self.menu = WebElement(browser=self.browser,
                               locator=self.MENU,
                               description="Frames Page -> Collapse Menu Alerts, Frames & Windows container")
        self.menu_item = WebElement(browser=self.browser,
                                    locator=self.MENU_ELEMENT_ITEM,
                                    description="Frames Page -> Alerts, Frames & Windows menu item list container")
        self.nested_frames_menu_item = Label(browser=self.browser,
                                             locator=self.MENU_ITEM,
                                             description="Frames Page -> Nested Frames menu item")
        self.nested_frames_page = NestedFramesPage(browser)

    def click_menu(self) -> None:
        self.menu.click()

    def click_menu_item(self) -> None:
        self.nested_frames_menu_item.click()

    def is_menu_exists(self) -> bool:
        return self.menu.is_exists()

    def is_parent_frame_text_visible(self) -> bool:
        return self.nested_frames_page.is_parent_frame_text_exists()

    def is_child_frame_text_visible(self) -> bool:
        return self.nested_frames_page.is_child_frame_text_exists()

