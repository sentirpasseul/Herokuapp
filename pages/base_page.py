import pytest
from core.browser import Browser
from utils.logs.logger import Logger


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    def __init__(self, browser: Browser):
        self.browser = browser
        self.page_name = None
        self.unique_element = None

    def wait_for_open(self) -> None:
        Logger.info(f"Waiting for open page {self.page_name}")
        self.unique_element.wait_for_presence()
