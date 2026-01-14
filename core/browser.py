from selenium.webdriver.remote.webdriver import WebDriver, WebDriverException
from utils.logs.logger import Logger
from selenium.common.exceptions import NoAlertPresentException
from elements.base_element import BaseElement
from selenium.webdriver import ActionChains


class Browser:
    DEFAULT_TIMEOUT = 10
    PAGE_LOAD_TIMEOUT = 20

    def __init__(self, driver: WebDriver):
        self._driver = driver

        self.main_handle = None
        self.alert = None
        self.original_window = self._driver.current_window_handle
        self.actions = ActionChains(driver)

    @property
    def driver(self):
        return self._driver

    @property
    def current_url(self):
        return self._driver.current_url

    def get(self, url: str) -> None:
        Logger.info(f"Get: {url}")
        try:
            self._driver.get(url)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        self.main_handle = self._driver.current_window_handle

    def close(self):
        Logger.info(f"{self}: close window handle = '{self._driver.current_window_handle}'")
        self._driver.close()

    def quit(self):
        Logger.info(f"{self}: quit")
        try:
            self._driver.quit()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def refresh(self):
        Logger.info("Page refresh")
        self._driver.refresh()

    def switch_to_alert(self):
        try:
            self.alert = self._driver.switch_to.alert
            Logger.info(f"Switch to alert: {self.alert}")
            return self.alert
        except NoAlertPresentException as err:
            Logger.error(f"Failed to switch to alert: {err}")
            return NoAlertPresentException

    def get_alert_text(self):
        self.switch_to_alert()
        text = self.alert.text
        Logger.info(f"Get alert text: {text}")
        return text

    def confirm_alert(self):
        Logger.info(f"Confirm alert: {self.alert.text}")
        self.alert.accept()

    def switch_to_frame(self, frame: BaseElement):
        Logger.info(f"Switch to frame: {frame}")
        self._driver.switch_to.frame(frame.wait_for_presence())

    def switch_to_window(self, window):
        Logger.info(f"Switch to window: {window}")
        self._driver.switch_to.window(window)

    def send_keys_alert(self, value: str):
        Logger.info(f"Send {value} successful")
        self._driver.switch_to.alert.send_keys(value)

    def execute_script(self, script, *args):
        Logger.info(f"Execute script: {script}")
        return self._driver.execute_script(script, *args)

    def switch_to_new_tab(self):
        if not hasattr(self, 'original_window') or self.original_window is None:
            self.original_window = self._driver.current_window_handle

        all_handles = self._driver.window_handles
        if len(all_handles) > 1:
            self._driver.switch_to.window(all_handles[-1])
            Logger.info("Switch to new tab")
        else:
            raise Exception("No new tab found to switch to")

    def switch_to_original_window(self):
        Logger.info("Switch to original window")
        self.switch_to_window(self.original_window)

    def go_back(self):
        Logger.info(f"Back to previous window")
        self._driver.back()

    def get_title(self):
        Logger.info(f"Get title current page")
        return self._driver.title

    def scroll_to_element(self, element):
        self._driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'})",
            element
        )

    def click_button_with_js(self, selector: str) -> None:
        script = f"document.querySelector('[onClick=\"{selector}\"]').click();"
        self.execute_script(script)

    def get_text_with_js(self, selector: str):
        script = f"return document.getElementById('{selector}').innerText;"
        return self.execute_script(script)
