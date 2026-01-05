from selenium.webdriver.remote.webdriver import WebDriver, WebDriverException
from utils.logs.logger import Logger
from selenium.common.exceptions import NoAlertPresentException
from elements.base_element import BaseElement


class Browser:
    DEFAULT_TIMEOUT = 10
    PAGE_LOAD_TIMEOUT = 20

    def __init__(self, driver: WebDriver):
        self._driver = driver

        self.main_handle = None
        self.alert = None
        self.original_window = self._driver.current_window_handle

    @property
    def driver(self):
        return self._driver

    @property
    def current_url(self):
        return self._driver.current_url

    def get(self, url: str) -> None:
        Logger.info(f"{self} get: {url}")
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
        self._driver.execute_script(script, *args)

    def switch_to_new_tab(self):
        for handle in self._driver.window_handles:
            if handle != self.original_window:
                self.switch_to_window(handle)

    def switch_to_original_window(self):
        self.switch_to_window(self.original_window)

    def go_back(self):
        self._driver.back()

    def get_title_current_page(self):
        return self._driver.title
