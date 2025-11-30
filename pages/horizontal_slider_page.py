import random

from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from utils.logs.logger import Logger

class HorizontalSliderPage(BasePage):

    HORIZONTAL_SLIDER_PAGE_LINK = "http://the-internet.herokuapp.com/horizontal_slider"
    HORIZONTAL_SLIDER_PAGE_UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Horizontal Slider')]"
    HORIZONTAL_SLIDER_INPUT_LOC = "//input[@type='range']"
    HORIZONTAL_SLIDER_COUNT = "//*[@id='range']"

    def __init__(self, browser, test_value):
        super().__init__(browser)
        self.unique_element = self.element(browser=browser, locator=self.HORIZONTAL_SLIDER_PAGE_UNIQUE_LOC)
        self.browser = browser
        self.test_value = test_value

    def open(self):
        try:
            self.browser.get(self.HORIZONTAL_SLIDER_PAGE_LINK)
            self.wait_for_open()
            return True
        except TimeoutException as err:
            return False

    def check_horizontal_slider(self):
        try:
            slider = self.element(browser=self.browser, locator=self.HORIZONTAL_SLIDER_INPUT_LOC)
            slider.wait_for_visible()
            slider.slide_horizontal(self.test_value)
            counter = self.element(browser=self.browser, locator=self.HORIZONTAL_SLIDER_COUNT)
            counter.wait_for_visible()
            if counter.get_text() == self.test_value:
                Logger.info(f"Check horizontal slider is successful: {counter.get_text()} = {self.test_value}")
                return True
        except TimeoutException as err:
            Logger.error(f"Failed to check horizontal slider: {err}")
            return False

