import random
from enum import StrEnum

from pages.horizontal_slider_page import HorizontalSliderPage

class TestHorizontalSlider:

    @staticmethod
    def get_random_float_from_range():
        return random.uniform(0.0, 5.0)

    def test_horizontal_slider(self, browser):
        horizontal_slider = HorizontalSliderPage(browser, self.get_random_float_from_range())
        assert horizontal_slider.open()
        assert horizontal_slider.check_horizontal_slider()