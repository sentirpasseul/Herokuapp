from selenium.webdriver.common.by import By
from core.browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from utils.logs.logger import Logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains

class BaseElement:
    DEFAULT_TIMEOUT = 10

    def __init__(self,
                 browser: Browser,
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

    def wait_for_presence(self) -> WebElement:
        return self.wait_for(expected_condition=expected_conditions.presence_of_element_located)

    def wait_for_clickable(self) -> WebElement:
        return self.wait_for(expected_condition=expected_conditions.element_to_be_clickable)

    def wait_for_visible(self) -> WebElement:
        return self.wait_for(expected_condition=expected_conditions.visibility_of_element_located)

    def click(self):
        self.wait_for(expected_condition=expected_conditions.element_to_be_clickable).click()

    def get_text(self):
        return self.wait_for(expected_condition=expected_conditions.visibility_of_element_located).text

    def get_attribute(self, name: str):
        return self.wait_for(expected_condition=expected_conditions.presence_of_element_located).get_attribute(name)

    def is_enabled(self):
        return self.wait_for(expected_condition=expected_conditions.visibility_of_element_located).is_enabled()

    def move_mouse_to_div(self):
        element = self.wait_for_visible()
        self.actions.move_to_element(element)

    def right_click(self):
        self.actions.context_click().perform()

    def send_keys(self, value):
        self.actions.send_keys(value).perform()

    def slide_horizontal(self, value: float):
        element = self.wait_for_visible()
        width = element.size['width']
        min_val = float(element.get_attribute("min"))
        max_val = float(element.get_attribute("max"))
        step = float(element.get_attribute("step"))

        pixels_per_step = width / ((max_val-min_val)/step)
        steps = int((value-min_val)/step)
        self.actions.click_and_hold(element).move_by_offset(pixels_per_step * steps, 0).release().perform()



