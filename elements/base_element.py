from selenium.webdriver.common.by import By
from core.browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from utils.logs.logger import Logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions

class BaseElement:
    DEFAULT_TIMEOUT = 10

    def __init__(self,
                 browser: Browser,
                 locator: str | tuple,
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

    def wait_for(self, expected_condition) -> WebElement:
        try:
            Logger.info(f"{self.description} wait for {expected_condition.__name__}")
            element = self._wait.until(method=expected_condition(self.locator))
            return element
        except TimeoutException as err:
            Logger.error(f"{self.description}: {err}")
            raise

    def wait_for_not(self, expected_condition) -> WebElement:
        try:
            Logger.info(f"{self.description} wait for not {expected_condition.__name__}")
            element = self._wait.until_not(method=expected_condition(self.locator))
            return element
        except TimeoutException as err:
            Logger.error(f"{self.description}: {err}")
            raise

    def wait_for_presence(self):
        self.wait_for(expected_condition=expected_conditions.presence_of_element_located)

    def wait_for_clickable(self):
        self.wait_for(expected_condition=expected_conditions.element_to_be_clickable)

    def wait_for_visible(self):
        self.wait_for(expected_condition=expected_conditions.visibility_of_element_located)

    def click(self):
        self.wait_for(expected_condition=expected_conditions.element_to_be_clickable).click()

    def get_text(self):
        return self.wait_for(expected_condition=expected_conditions.visibility_of_element_located).text

    def get_attribute(self, name: str):
        return self.wait_for(expected_condition=expected_conditions.presence_of_element_located).get_attribute(name)

    def is_enabled(self):
        return self.wait_for(expected_condition=expected_conditions.visibility_of_element_located).is_enabled()


