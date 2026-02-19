import os
import platform
from enum import StrEnum
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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

            is_ci = os.getenv("CI", "false").lower() == "true"
            system = platform.system()

            if is_ci or system == "Linux":

                chrome_options.binary_location = os.getenv("CHROME_BIN", "/usr/bin/chromium")

                chrome_options.add_argument("--headless=new")
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument("--disable-dev-shm-usage")
                chrome_options.add_argument("--disable-gpu")

                driver_path = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")
                service = Service(executable_path=driver_path)
                return webdriver.Chrome(service=service, options=chrome_options)
            else:
                if "--headless" in options or os.getenv("HEADLESS", "false").lower() == "true":
                    chrome_options.add_argument("--headless=new")

            for option in options:
                chrome_options.add_argument(option)

            service = Service(ChromeDriverManager().install())
            return webdriver.Chrome(service=service, options=chrome_options)
        else:
            raise NotImplementedError(f"{driver_name} not implemented.")
