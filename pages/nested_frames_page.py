from pages.frames_page import BasePage
from elements.custom_elements.label import Label
from elements.custom_elements.web_element import WebElement
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

    def check_parent_iframe(self):
        self.browser.switch_to_frame(iframe)

        parent_frame_text.wait_for_visible()

    def check_child_iframe(self):
        self.browser.switch_to_frame(iframe)

        child_frame_text.wait_for_visible()
