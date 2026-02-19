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

    def wait_for_element_not_visible(self):
        return self.wait_for_not(expected_condition=expected_conditions.invisibility_of_element_located)

    def click(self):
        element = self.wait_for_clickable()
        Logger.info(f"{self} click")
        element.click()

    def get_text(self):
        element = self.wait_for_presence()
        Logger.info(f"Get text: {element}")
        return element.text

    def get_attribute(self, name: str):
        element = self.wait_for_presence()
        Logger.info(f"Get {self.locator} attribute by {name}")
        return element.get_attribute(name)

    def is_enabled(self):
        Logger.info(f"{self} is enabled")
        return self.wait_for(expected_condition=expected_conditions.visibility_of_element_located).is_enabled()

    def is_exists(self):
        try:
            Logger.info(f"{self} is exists")
            self.wait_for_presence()
            return True
        except TimeoutException:
            return False

    def move_mouse_to_element(self):
        try:
            element = self.wait_for_visible()
            Logger.info(f"Move mouse to {self}")
            self.actions.move_to_element(element).perform()
        except:
            Logger.error(f"Failed to move mouse to element: {self}")
            raise

    def context_click(self):
        try:
            element = self.wait_for_visible()
            Logger.info(f"{self} is right clicked")
            self.actions.context_click(element).perform()
        except:
            Logger.error(f"Failed to right click {self}")
            raise

    def open_context_menu(self):
        try:
            self.wait_for_visible()
            self.move_mouse_to_element()
            Logger.info("Open context menu")
            self.context_click()
        except:
            Logger.error("Failed to open context menu")
            raise

    def scroll_to_element(self, block='center', behavior='instant'):
        try:
            element = self.wait_for_visible()
            Logger.info(f"Scroll to {element}: (block={block}, behavior={behavior}")
            self.browser.driver.execute_script(
                f"arguments[0].scrollIntoView({{block: '{block}', behavior: '{behavior}'}})", element)
            self.browser.execute_script("window.dispatchEvent(new Event('scroll'));", element)
        except:
            Logger.error(f"Ошибка при скролле элемента")
            raise

    def js_click(self) -> None:
        element = self.wait_for_presence()
        Logger.info(f"{element} javascript clicked")
        self.browser.execute_script("arguments[0].click()", element)

    def get_text_with_js(self):
        element = self.wait_for_presence()
        Logger.info("Get text with js")
        return self.browser.execute_script("return arguments[0].innerText;", element)

    def set_value_element(self, value):
        Logger.info(f"Set {value} to {self} ")
        element = self.wait_for_visible()
        self.browser.execute_script("arguments[0].value=arguments[1]", element, value)

    def dispatch_event_change(self):
        Logger.info("Dispatch Event change")
        element = self.wait_for_presence()
        self.browser.execute_script("arguments[0].dispatchEvent(new Event('change',{ bubbles: true }))", element)

    def wait_for_frame_and_switch(self):
        try:
            Logger.info(f"Switch to frame: {self}")
            self.wait_for(expected_condition=expected_conditions.frame_to_be_available_and_switch_to_it)
        except:
            Logger.error(f"{self} not available to switch")
            raise
