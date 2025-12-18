from elements.base_element import BaseElement
from selenium.common.exceptions import WebDriverException

from utils.logs.logger import Logger


class Input(BaseElement):

    def send_keys(self, keys) -> None:
        element = self.wait_for_visible()
        self.clear()
        try:
            element.send_keys(keys)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def clear(self):
        element = self.wait_for_visible()
        element.clear()