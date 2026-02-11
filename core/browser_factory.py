import os
from enum import StrEnum
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from utils.logs.logger import Logger


class AvailableDriverName(StrEnum):
    CHROME = "chrome"


class BrowserFactory:
    @staticmethod
    def get_driver(
            driver_name: AvailableDriverName = AvailableDriverName.CHROME,
            options: list[str] = None
    ) -> WebDriver:
        if options is None:
            options = []

        print(f"DEBUG: All env vars: {dict(os.environ)}")
        remote_url = os.getenv("SELENIUM_REMOTE_URL")

        Logger.info(f"Start webdriver: {driver_name} | Remote: {bool(remote_url)} | Options: '{options}'")
        if driver_name == AvailableDriverName.CHROME:
            chrome_options = webdriver.ChromeOptions()

            chrome_options.add_argument("--headless=new")  # Самый важный флаг
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")

            for option in options:
                chrome_options.add_argument(option)

            if remote_url:
                return webdriver.Remote(
                    command_executor=remote_url,
                    options=chrome_options
                )

            return webdriver.Chrome(options=chrome_options)

        else:
            raise NotImplementedError(f"{driver_name} not implemented.")
