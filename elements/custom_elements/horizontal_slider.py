from elements.base_element import BaseElement

class HorizontalSlider(BaseElement):

    def set_value_in_slider(self, value):
        element = self.wait_for_visible()
        element.send_keys(value)