import random
from config.urls import URLs
from pages.horizontal_slider_page import HorizontalSliderPage


class TestHorizontalSlider:

    @staticmethod
    def get_random_float_from_range(min_value: float, max_value: float, step):
        steps_count = random.randrange(0, int((max_value - min_value) / step) + 1)
        return min_value + (steps_count * step)

    def test_horizontal_slider(self, browser):
        browser.get(URLs.HORIZONTAL_SLIDER_PAGE)
        horizontal_slider = HorizontalSliderPage(browser)
        random_value = self.get_random_float_from_range(min_value=horizontal_slider.get_min_range(),
                                                        max_value=horizontal_slider.get_max_range(),
                                                        step=horizontal_slider.get_step_range())
        assert horizontal_slider.open(), "Ошибка при открытии страницы с горизонтальным слайдером \n"
        assert horizontal_slider.check_horizontal_slider(
            random_value),  "Ошибка при проверке горизонтального слайдера \n"



