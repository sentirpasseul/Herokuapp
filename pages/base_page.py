from core.browser import Browser
from utils.logs.logger import Logger
from selenium.common.exceptions import TimeoutException
from elements.base_element import BaseElement


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    def __init__(self, browser: Browser):
        self.browser = browser
        self.page_name = self.__class__.__name__
        self.unique_element = None
        self.element = BaseElement

    def wait_for_open(self):
        try:
            self.unique_element.wait_for_presence()
            Logger.info(f"Open {self.page_name} successfully")
            return True
        except TimeoutException as err:
            Logger.error(f"Failed open {self.page_name}: {err}")
            return False

