import random

from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from utils.logs.logger import Logger
from elements.base_element import BaseElement
from elements.custom_elements.horizontal_slider import HorizontalSlider


class HorizontalSliderPage(BasePage):
    HORIZONTAL_SLIDER_PAGE_UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Horizontal Slider')]"
    HORIZONTAL_SLIDER_INPUT_LOC = "//input[@type='range']"
    HORIZONTAL_SLIDER_COUNT = "range"

    def __init__(self, browser):
        super().__init__(browser)
        self.base_element = BaseElement(browser)
        self.unique_element = self.HORIZONTAL_SLIDER_PAGE_UNIQUE_LOC
        self.browser = browser
        self.slider = HorizontalSlider(browser)

    def open(self):
        try:
            self.wait_for_open()
            return True
        except TimeoutException:
            return False

    def get_min_range(self):
        return self.base_element.get_attribute("min")

    def get_max_range(self):
        return self.base_element.get_attribute("max")

    def get_step_range(self):
        return self.base_element.get_attribute("step")

    def check_horizontal_slider(self, test_value):
        try:
            slider = self.slider
            slider.wait_for_visible()
            slider.set_value_in_slider(test_value)
            counter = self.element(locator=self.HORIZONTAL_SLIDER_COUNT)
            counter.wait_for_visible()
            if counter.get_text() == test_value:
                Logger.info(f"Check horizontal slider is successful: {counter.get_text()} = {test_value}")
                return True
        except TimeoutException as err:
            Logger.error(f"Failed to check horizontal slider: {err}")
            return False
