from elements.base_element import BaseElement


class Label(BaseElement):

    @property
    def text(self):
        return f"{self.get_text()}"
