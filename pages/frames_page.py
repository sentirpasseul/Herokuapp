from pages.base_page import BasePage
from pages.nested_frames_page import NestedFramesPage
from selenium.common.exceptions import TimeoutException
from elements.custom_elements.label import Label
from elements.custom_elements.container import Container


class FramePage(BasePage):
    FRAME_PAGE_UNIQUE_LOC = "//div[@id='framesWrapper']//*[contains(text(), 'Frames')]"
    FRAME_PAGE_MENU_ELEMENT_ITEM = "//div[@class= 'element-list collapse show']//*[contains(text(), 'Browser Windows')]"
    FRAME_PAGE_MENU = "//*[text()='Browser Windows']/ancestor::div[@class='element-group']//span[@class='group-header']"
    NESTED_FRAMES_MENU_ITEM = "//div[@class= 'element-group']//*[contains(text(), 'Nested Frames')]"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.FRAME_PAGE_UNIQUE_LOC,
                                    description="Frames Page -> Frames Page Label")
        self.nested_frames_page = NestedFramesPage(browser)

    def check_collapse_menu(self):
        try:
            menu_item = Container(browser=self.browser,
                                  locator=self.FRAME_PAGE_MENU_ELEMENT_ITEM,
                                  description="Frames Page -> Alerts, Frames & Windows menu item list container")
            menu = Container(browser=self.browser,
                             locator=self.FRAME_PAGE_MENU,
                             description="Frames Page -> Collapse Menu Alerts, Frames & Windows container")
            nested_frames_menu_item = Label(browser=self.browser,
                                            locator=self.NESTED_FRAMES_MENU_ITEM,
                                            description="Frames Page -> Nested Frames menu item")
            if menu_item.wait_for_element_not_visible():
                menu.click()
            nested_frames_menu_item.wait_for_visible()
            nested_frames_menu_item.click()
            return True
        except TimeoutException:
            return False
