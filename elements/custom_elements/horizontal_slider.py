from elements.custom_elements.web_element import WebElement
from utils.logs.logger import Logger


class HorizontalSlider(WebElement):

    def set_value_to_slider(self, value):
        Logger.info(f"Set {value} to {self}")
        self.wait_for_visible()
        self.set_value_element(value=value)
        self.dispatch_event_change()

    def get_min_range(self) -> float:
        return float(self.get_attribute("min"))

    def get_max_range(self) -> float:
        return float(self.get_attribute("max"))

    def get_step_range(self) -> float:
        return float(self.get_attribute("step"))
