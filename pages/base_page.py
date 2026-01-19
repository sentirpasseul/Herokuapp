from core.browser import Browser
from utils.logs.logger import Logger


class BasePage:

    def __init__(self, browser: Browser):
        self.browser = browser
        self.page_name = None
        self.unique_element = None

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.page_name}]"

    def __repr__(self) -> str:
        return str(self)

    def wait_for_open(self):
        Logger.info(f"{self}: wait for open")
        self.unique_element.wait_for_presence()
