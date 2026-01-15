from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from utils.logs.logger import Logger
from selenium.common.exceptions import TimeoutException, JavascriptException, StaleElementReferenceException
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
        Logger.info(f"Clicked element: {self}")
        self.wait_for_clickable().click()

    def get_text(self):
        text = self.wait_for(expected_condition=expected_conditions.visibility_of_element_located).text
        Logger.info(f"Get text: {text}")
        return text

    def get_attribute(self, name: str):
        attribute = self.wait_for_presence().get_attribute(name)
        Logger.info(f"Get attribute: {attribute}")
        return attribute

    def is_enabled(self):
        Logger.info(f"{self} is enabled")
        return self.wait_for(expected_condition=expected_conditions.visibility_of_element_located).is_enabled()

    def is_displayed(self):
        Logger.info(f"{self} is displayed")
        return self.wait_for(expected_condition=expected_conditions.visibility_of_element_located).is_displayed()

    def move_mouse_to_element(self):
        element = self.wait_for_visible()
        Logger.info(f"Move mouse to {element}")
        self.actions.move_to_element(element).perform()

    def context_click(self):
        Logger.info("Right click")
        self.actions.context_click().perform()

    def open_context_menu(self):
        self.wait_for_visible()
        self.move_mouse_to_element()
        Logger.info("Open context menu")
        self.context_click()

    def scroll_to_element(self, block='center', behavior='smooth'):
        try:
            element = self.wait_for_visible()
            self.browser.driver.execute_script(
                f"arguments[0].scrollIntoView({{block: '{block}', behavior: '{behavior}'}})", element)
            Logger.info(f"Скролл к элементу (block={block}, behavior={behavior}")
        except StaleElementReferenceException:
            Logger.warning(f"{self} устарел, попытка заново найти и проскроллить")
            try:
                element = self.wait_for_visible()
                self.browser.driver.execute_script(
                    f"arguments[0].scrollIntoView({{block: '{block}', behavior: '{behavior}'}});",
                    element
                )
                Logger.info(f"{self} попытка скролла удалась после повторного поиска элемента")
            except StaleElementReferenceException:
                Logger.error(f"{self} остался устаревшим после повторной попытки")
                raise

        except JavascriptException as e:
            Logger.error(f"{self} JavaScript error during scroll: {e}")
            raise

        except Exception as e:
            Logger.error(f"{self} unexpected error during scroll: {e}")
            raise

    def js_click(self) -> None:
        element = self.wait_for_visible()
        Logger.info(f"{element} javascript clicked")
        self.browser.execute_script("arguments[0].click()", element)

    def get_text_with_js(self):
        element = self.wait_for_visible()
        Logger.info("Get text with js")
        return self.browser.execute_script("return arguments[0].innerText;", element)

    def set_value_to_element(self, value, element):
        Logger.info(f"Set {value} to {element} ")
        self.browser.execute_script("arguments[0].value=arguments[1]", element, value)

    def dispatch_event_change(self, element):
        Logger.info("Dispatch Event change")
        self.browser.execute_script("arguments[0].dispatchEvent(new Event('change',{ bubbles: true }))", element)

