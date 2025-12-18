import random
from config.urls import URLs
from pages.horizontal_slider_page import HorizontalSliderPage


class TestHorizontalSlider:

    @staticmethod
    def get_random_float_from_range(min_value, max_value, step):
        return random.randint(min_value, max_value) * step

    def test_horizontal_slider(self, browser):
        browser.get(URLs.HORIZONTAL_SLIDER_PAGE)
        horizontal_slider = HorizontalSliderPage(browser)
        assert horizontal_slider.check_horizontal_slider(
            1), "Ошибка при проверке горизонтального слайдера \n"
        random_value = self.get_random_float_from_range(min_value=horizontal_slider.get_min_range(),
                                                        max_value=horizontal_slider.get_max_range(),
                                                        step=horizontal_slider.get_step_range())

        assert horizontal_slider.open(), "Ошибка при открытии страницы с горизонтальным слайдером \n"

