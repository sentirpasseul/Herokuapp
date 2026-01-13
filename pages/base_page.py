from core.browser import Browser
from utils.logs.logger import Logger
from elements.base_element import BaseElement
from elements.common.alert_handler import AlertHandler


class BasePage:

    def __init__(self, browser: Browser):
        self.browser = browser
        self.page_name = None
        self.unique_element = None
        self.alerts = AlertHandler(browser)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.page_name}]"

    def __repr__(self) -> str:
        return str(self)

    def element(self, locator: str | tuple, description: str = None) -> BaseElement:
        return BaseElement(
            browser=self.browser,
            locator=locator,
            description=description
        )

    def wait_for_open(self):
        Logger.info(f"{self}: wait for open")
        self.unique_element.wait_for_presence()

    @property
    def get_current_url(self):
        return self.browser.current_url
