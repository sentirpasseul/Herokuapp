from elements.base_element import BaseElement


class Label(BaseElement):

    def with_text(self, text):
        by, locator_value = self.locator
        return Label(browser=self.browser,
                     locator=(by, locator_value),
                     description=f"{self.description} with text {text}")
