from elements.base_element import BaseElement


class Label(BaseElement):

    def with_text(self, text):
        by, locator_value = self.locator
        new_locator_value = locator_value.format(text=text)
        return Label(browser=self.browser,
                     locator=(by, new_locator_value),
                     description=f"{self.description} with text {text}")
