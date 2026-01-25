from pages.frames_page import BasePage
from elements.custom_elements.label import Label
from elements.custom_elements.web_element import WebElement


class NestedFramesPage(BasePage):
    UNIQUE_LOC = "//*[@id='framesWrapper']//*[contains(text(), 'Nested Frames')]"
    IFRAME_PARENT_CONTAINER = "frame1"
    PARENT_FRAME_LABEL = "//*[contains(text(), 'Parent frame')]"
    IFRAME_CHILD_CONTAINER = "//*[contains(@srcdoc,'Child Iframe')]"
    CHILD_FRAME_LABEL = "//*[contains(text(), 'Child Iframe')]"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Nested Frames Page -> Nested Frames label")
        self.iframe = WebElement(browser=self.browser,
                                 locator=self.IFRAME_PARENT_CONTAINER,
                                 description="Nested Frames Page -> Iframe parent container")
        self.iframe_child = WebElement(browser=self.browser,
                                       locator=self.IFRAME_CHILD_CONTAINER,
                                       description="Nested Frames Page -> Iframe child container")
        self.parent_frame_text = Label(browser=self.browser,
                                       locator=self.PARENT_FRAME_LABEL,
                                       description="Nested Frames Page -> Parent frame text")
        self.child_frame_text = Label(browser=self.browser,
                                      locator=self.CHILD_FRAME_LABEL,
                                      description="Nested Frames Page -> Child frame text")

    def is_parent_frame_text_exists(self):
        return self.parent_frame_text.is_exists()

    def is_child_frame_text_exists(self):
        return self.child_frame_text.is_exists()

    def switch_to_iframe(self) -> None:
        self.iframe.wait_for_frame_and_switch()

    def switch_to_iframe_child(self) -> None:
        self.iframe_child.wait_for_frame_and_switch()