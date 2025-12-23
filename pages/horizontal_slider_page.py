import random

from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from utils.logs.logger import Logger
from elements.custom_elements.horizontal_slider import HorizontalSlider
from elements.custom_elements.label import Label
from elements.custom_elements.input import Input


class HorizontalSliderPage(BasePage):
    HORIZONTAL_SLIDER_PAGE_UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Horizontal Slider')]"
    HORIZONTAL_SLIDER_INPUT_LOC = "//input[@type='range']"
    HORIZONTAL_SLIDER_COUNT = "range"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser=browser, locator=self.HORIZONTAL_SLIDER_PAGE_UNIQUE_LOC,
                                    description="Horizontal Slider Page -> Label")
        self.browser = browser
        self.slider = HorizontalSlider(browser=browser, locator=self.HORIZONTAL_SLIDER_INPUT_LOC,
                                       description="Horizontal Slider Page -> Horizontal Slider input")
        self.counter = Label(browser=browser, locator=self.HORIZONTAL_SLIDER_COUNT,
                             description="Horizontal Slider Page -> Counter label")

    def open(self):
        try:
            self.wait_for_open()
            return True
        except TimeoutException:
            return False

    def get_min_range(self):
        return float(self.slider.get_attribute("min"))

    def get_max_range(self):
        return float(self.slider.get_attribute("max"))

    def get_step_range(self):
        return float(self.slider.get_attribute("step"))

    def get_counter_text(self):
        return self.counter.text

    def check_horizontal_slider(self, test_value):
        try:
            self.slider.wait_for_visible()
            self.slider.set_value_to_slider(test_value)
            counter = self.get_counter_text()
            if float(counter) == float(test_value):
                Logger.info(f"Check horizontal slider: {float(counter)} = {float(test_value)}")
                return True
        except TimeoutException as err:
            Logger.error(f"Failed to check horizontal slider: {err}")
            return False
