from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from utils.logs.logger import Logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from typing import List


class BaseElement:
    DEFAULT_TIMEOUT = 10

    def __init__(self,
                 browser,
                 locator: str | tuple | None = None,
                 description: str = None,
                 timeout: int = DEFAULT_TIMEOUT):
        self.browser = browser
        self.timeout = timeout

        if isinstance(locator, str):
            if "/" in locator:
                self.locator = (By.XPATH, locator)
            else:
                self.locator = (By.ID, locator)
        else:
            self.locator = locator

        self.description = description if description else str(locator)
        self._wait = WebDriverWait(self.browser.driver, timeout=self.timeout)
        self.actions = ActionChains(self.browser.driver)

    @property
    def element(self):
        return self.wait_for_presence()

    @property
    def text(self):
        return f"{self.get_text()}"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)

    def wait_for(self, expected_condition) -> WebElement:
        try:
            Logger.info(f"{self} wait for {expected_condition.__name__}")
            return self._wait.until(method=expected_condition(self.locator))
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            raise

    def wait_for_elements(self, expected_condition) -> List[WebElement]:
        try:
            Logger.info(f"{self} wait for {expected_condition.__name__}")
            return self._wait.until(method=expected_condition(self.locator))
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            raise

    def wait_for_not(self, expected_condition) -> None:
        try:
            Logger.info(f"{self} wait for not {expected_condition.__name__}")
            element = self._wait.until_not(method=expected_condition(self.locator))
            return element
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            raise

    def wait_for_presence(self) -> WebElement:
        return self.wait_for(expected_condition=expected_conditions.presence_of_element_located)

    def wait_for_clickable(self) -> WebElement:
        return self.wait_for(expected_condition=expected_conditions.element_to_be_clickable)

    def wait_for_visible(self) -> WebElement:
        return self.wait_for(expected_condition=expected_conditions.visibility_of_element_located)

    def wait_for_all_visible(self) -> List[WebElement]:
        return self.wait_for_elements(expected_condition=expected_conditions.visibility_of_all_elements_located)

    def wait_for_element_not_visible(self):
        return self.wait_for_not(expected_condition=expected_conditions.invisibility_of_element_located)

    def click(self):
        try:
            self.wait_for(expected_condition=expected_conditions.element_to_be_clickable).click()
            Logger.info(f"Clicked element: {self}")
        except TimeoutException as err:
            Logger.error(f"Failed to click element {self}: {err}")
            return False

    def get_text(self):
        try:
            text = self.wait_for(expected_condition=expected_conditions.visibility_of_element_located).text
            Logger.info(f"Get text: {text}")
            return text
        except TimeoutException as err:
            Logger.error(f"Failed to get text: {err}")
            return False

    def get_attribute(self, name: str):
        return self.wait_for_presence().get_attribute(name)

    def is_enabled(self):
        return self.wait_for(expected_condition=expected_conditions.visibility_of_element_located).is_enabled()

    def move_mouse_to_div(self):
        div = self.wait_for_visible()
        self.actions.move_to_element(div).perform()

    def right_click(self):
        self.actions.context_click().perform()
