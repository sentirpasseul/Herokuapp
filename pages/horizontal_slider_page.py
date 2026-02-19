import random

from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from utils.logs.logger import Logger
from elements.custom_elements.horizontal_slider import HorizontalSlider
from elements.custom_elements.label import Label
from elements.custom_elements.input import Input


class HorizontalSliderPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Horizontal Slider')]"
    INPUT_LOC = "//input[@type='range']"
    COUNTER = "range"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Horizontal Slider Page -> Label")
        self.slider = HorizontalSlider(browser=browser,
                                       locator=self.INPUT_LOC,
                                       description="Horizontal Slider Page -> Horizontal Slider input")
        self.counter = Label(browser=browser,
                             locator=self.COUNTER,
                             description="Horizontal Slider Page -> Counter label")

    def set_value_to_horizontal_slider(self, value):
        self.slider.set_value_to_slider(value)

    def get_min_range_slider(self):
        return self.slider.get_min_range()

    def get_max_range_slider(self):
        return self.slider.get_max_range()

    def get_step_rang_slider(self):
        return self.slider.get_step_range()

    def get_counter_text(self):
        return float(self.counter.get_text())
