from elements.custom_elements.input import Input
from utils.logs.logger import Logger


class HorizontalSlider(Input):

    def __init__(self, browser, locator, description):
        super().__init__(browser=browser, locator=locator, description=description)

    def set_value_to_slider(self, value):
        element = self.wait_for_visible()
        self.set_value_to_element(value=value, element=element)
        self.dispatch_event_change(element)
        Logger.info(f"Set {value} to {element}")


