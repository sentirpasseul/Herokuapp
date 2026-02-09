from core.browser import Browser
from elements.custom_elements.web_element import WebElement
from typing import Self


class MultiWebElement:
    DEFAULT_TIMEOUT = 10
    TIMEOUT_FOR_ELEMENTS = 5

    def __init__(
            self,
            browser: Browser,
            formatable_xpath: str,
            description: str = None,
            timeout: int = None
    ) -> None:
        self.index = 1

        self.browser = browser
        self.formatable_xpath = formatable_xpath
        self.description = description if description else self.formatable_xpath.format("'index'")
        self.timeout = timeout if timeout is not None else self.DEFAULT_TIMEOUT

    def __iter__(self) -> Self:
        self.index = 1
        return self

    def __next__(self) -> WebElement:
        current_element = WebElement(
            browser=self.browser,
            locator=self.formatable_xpath.format(index=self.index),
            description=f"{self.description}[{self.index}]",
            timeout=self.TIMEOUT_FOR_ELEMENTS
        )
        if not current_element.is_exists():
            raise StopIteration

        self.index += 1
        return current_element


def __str__(self) -> str:
    return f"{self.__class__.__name__}[{self.description}]"


def __repr__(self) -> str:
    return str(self)


def __getitem__(self, index: int) -> WebElement:
    xpath_index = index + 1
    return WebElement(
        browser=self.browser,
        locator=self.formatable_xpath.format(index=xpath_index),
        description=f"{self.description}[{xpath_index}]",
        timeout=self.timeout
    )


def get_count(self):
    elements = WebElement(browser=self.browser)
