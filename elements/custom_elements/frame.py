from elements.base_element import BaseElement


class Frame(BaseElement):

    def switch_to_frame(self):
        try:
            frame = self.wait_for_visible()
            self.browser.driver.switch_to.frame(frame)
        except:
            raise
