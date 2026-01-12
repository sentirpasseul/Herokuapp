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
        random_value = float(self.get_random_float_from_range(min_value=horizontal_slider.get_min_range(),
                                                        max_value=horizontal_slider.get_max_range(),
                                                        step=horizontal_slider.get_step_range()))

        horizontal_slider.wait_for_open()
        horizontal_slider.slider.set_value_to_slider(random_value)
        slider_counter = horizontal_slider.get_counter_text()
        assert slider_counter == random_value, (f"Ошибка при проверке значения слайдера\n"
                                                f"Actual: {slider_counter}\n"
                                                f"Expected: {random_value}\n")
