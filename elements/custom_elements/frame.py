from elements.base_element import BaseElement


class Frame(BaseElement):

    def switch_to_frame(self, frame):
        self.browser.switch_to_frame(frame)
