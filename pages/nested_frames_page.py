from pages.frames_page import BasePage
from elements.custom_elements.label import Label
from elements.custom_elements.web_element import WebElement
from elements.custom_elements.frame import Frame
from selenium.common.exceptions import TimeoutException


class NestedFramesPage(BasePage):
    UNIQUE_LOC = "//div[@id='framesWrapper']//*[contains(text(), 'Nested Frames')]"
    IFRAME_PARENT_CONTAINER = "frame1"
    PARENT_FRAME_LABEL = "//*[contains(text(), 'Parent frame')]"
    IFRAME_CHILD_CONTAINER = "//*[contains(@srcdoc,'Child Iframe')]"
    CHILD_FRAME_LABEL = "//*[contains(text(), 'Child Iframe')]"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Nested Frames Page -> Nested Frames label")
        self.iframe = Frame(browser=self.browser,
                            locator=self.IFRAME_PARENT_CONTAINER,
                            description="Nested Frames Page -> Iframe parent container")
        self.iframe_child = Frame(browser=self.browser,
                                  locator=self.IFRAME_CHILD_CONTAINER,
                                  description="Nested Frames Page -> Iframe child container")
        self.parent_frame_text = Label(browser=self.browser,
                                       locator=self.PARENT_FRAME_LABEL,
                                       description="Nested Frames Page -> Parent frame text")
        self.child_frame_text = Label(browser=self.browser,
                                      locator=self.CHILD_FRAME_LABEL,
                                      description="Nested Frames Page -> Child frame text")

    def get_child_frame(self):
        pass
