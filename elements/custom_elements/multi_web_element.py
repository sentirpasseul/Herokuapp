from elements.custom_elements.web_element import WebElement
from typing import List
from selenium.webdriver.support import expected_conditions


class MultiWebElement(WebElement):
    def wait_for_all_visible(self) -> List[WebElement]:
        return self.wait_for_elements(expected_condition=expected_conditions.visibility_of_all_elements_located)
