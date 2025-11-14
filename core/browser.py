from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver, WebDriverException
from utils.logs.logger import Logger

class Browser:
    DEFAULT_TIMEOUT = 10


    def __init__(self, driver: WebDriver):
        self._driver = driver

        self.main_handle = None

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





