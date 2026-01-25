from selenium.webdriver.remote.webdriver import WebDriver, WebDriverException

from elements.custom_elements.web_element import WebElement
from utils.logs.logger import Logger
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains


class Browser:
    DEFAULT_TIMEOUT = 10
    PAGE_LOAD_TIMEOUT = 20

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self.alert = None
        self.main_handle = None
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
        try:
            Logger.info("Page refresh")
            self._driver.refresh()
        except:
            Logger.error("Failed to refresh page ")
            raise

    def switch_to_alert(self):
        try:
            self.alert = self._driver.switch_to.alert
            Logger.info(f"Switch to alert: {self.alert}")
            return self.alert
        except NoAlertPresentException:
            Logger.error("Failed to switch to alert: No alert present on page")
            raise

    def get_alert_text(self):
        try:
            self.switch_to_alert()
            text = self.alert.text
            Logger.info(f"Get alert text: {text}")
            return text
        except:
            Logger.error("Failed to get alert text")
            raise

    def confirm_alert(self):
        try:
            Logger.info(f"Confirm alert: {self.alert.text}")
            self.alert.accept()
        except:
            Logger.error(f"Failed to confirm alert: {self.alert}")
            raise

    def switch_to_window(self, window):
        try:
            Logger.info(f"Switch to window: {window}")
            self._driver.switch_to.window(window)
        except:
            Logger.error(f"Failed to switch to window: {window}")
            raise

    def send_keys_alert(self, value: str):
        try:
            Logger.info(f"Send {value} to {self}")
            self._driver.switch_to.alert.send_keys(value)
        except:
            Logger.error(f"Failed to send {value} to {self}")
            raise

    def execute_script(self, script, *args):
        try:
            Logger.info(f"Execute script: {script}")
            return self._driver.execute_script(script, *args)
        except:
            Logger.error(f"Failed to execute script: {script}")
            raise

    def switch_to_new_tab(self):
        if self.original_window is None:
            self.original_window = self._driver.current_window_handle

        try:
            all_handles = self._driver.window_handles
            self._driver.switch_to.window(all_handles[-1])
            Logger.info(f"Switch to new tab: {self.driver.current_window_handle}")
        except:
            Logger.error("Failed to switch to new tab")
            raise

    def switch_to_original_window(self):
        Logger.info("Switch to original window")
        self.switch_to_window(self.original_window)

    def go_back(self):
        try:
            Logger.info(f"Back to previous window")
            self._driver.back()
        except:
            Logger.error("failed to go back to previous window")
            raise

    def get_title(self):
        try:
            Logger.info(f"Get title current page")
            return self._driver.title
        except:
            Logger.error("Failed to get title current page")
            raise

    def close_extra_tabs(self) -> None:
        try:
            Logger.info("Close extra tabs")
            handles = self.driver.window_handles
            for handle in handles[1:]:
                self.driver.switch_to.window(handle)
                self.driver.close()
            self.switch_to_original_window()
        except:
            Logger.error("Failed to close extra tabs")
            raise
