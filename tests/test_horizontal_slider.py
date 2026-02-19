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
        horizontal_slider_page = HorizontalSliderPage(browser)
        horizontal_slider_page.wait_for_open()

        random_value = float(self.get_random_float_from_range(min_value=horizontal_slider_page.get_min_range_slider(),
                                                              max_value=horizontal_slider_page.get_max_range_slider(),
                                                              step=horizontal_slider_page.get_step_rang_slider()))
        horizontal_slider_page.set_value_to_horizontal_slider(random_value)
        slider_counter = horizontal_slider_page.get_counter_text()
        assert slider_counter == random_value, (f"Ошибка при проверке значения слайдера\n"
                                                f"Actual: {slider_counter}\n"
                                                f"Expected: {random_value}\n")
