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
        self.unique_element = Label(browser=browser,
                                    locator=self.HORIZONTAL_SLIDER_PAGE_UNIQUE_LOC,
                                    description="Horizontal Slider Page -> Label")
        self.slider = HorizontalSlider(browser=browser,
                                       locator=self.HORIZONTAL_SLIDER_INPUT_LOC,
                                       description="Horizontal Slider Page -> Horizontal Slider input")
        self.counter = Label(browser=browser,
                             locator=self.HORIZONTAL_SLIDER_COUNT,
                             description="Horizontal Slider Page -> Counter label")

    def get_min_range(self) -> float:
        return float(self.slider.get_attribute("min"))

    def get_max_range(self) -> float:
        return float(self.slider.get_attribute("max"))

    def get_step_range(self) -> float:
        return float(self.slider.get_attribute("step"))

    def get_counter_text(self) -> float:
        return float(self.counter.text)

