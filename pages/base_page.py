import pytest
from core.browser_factory import BrowserFactory
from utils.logs.logger import Logger


class BasePage:
    def __init__(self):
        self.browser = BrowserFactory.get_driver()
        self.name = ""

    def wait_for_open(self):
        Logger.info(f"Waiting for open page {self.name}")
        ...