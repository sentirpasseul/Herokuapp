from elements.base_element import BaseElement
from elements.custom_elements.web_element import WebElement
from typing import List
from selenium.webdriver.support import expected_conditions
from utils.logs.logger import Logger
from selenium.common.exceptions import TimeoutException


class MultiWebElement(BaseElement):

    def wait_for_elements(self, expected_condition) -> List[WebElement]:
        try:
            Logger.info(f"{self} wait for {expected_condition.__name__}")
            return self._wait.until(method=expected_condition(self.locator))
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            raise

    def wait_for_all_visible(self) -> List[WebElement]:
        return self.wait_for_elements(expected_condition=expected_conditions.visibility_of_all_elements_located)
