from pages.base_page import BasePage
from utils.logs.logger import Logger
from selenium.common.exceptions import TimeoutException
from elements.base_element import BaseElement
from selenium.webdriver.common.by import By

class AuthPage(BasePage):
    AUTH_PAGE_LINK = "http://the-internet.herokuapp.com/basic_auth"

    def __init__(self, browser):
        super().__init__(browser)
        self.alert = None
        self.alert_text = str
        self.browser = browser
        self.success_message = BaseElement(locator='//div[contains(@class, "example")]//p[contains(text(), "Congratulations")]',
                                                   browser=self.browser)

    def auth(self, user: str, password: str):
        try:
            Logger.info(f"{self}: process of authorization")
            self.browser.get(f"https://{user}:{password}@the-internet.herokuapp.com/basic_auth")
            return True
        except TimeoutException as err:
            Logger.error(f"{err}: cannot authorize")
            return False

    def auth_success(self):
        try:
            self.success_message.wait_for_visible()
            Logger.info(f"Auth successful")
            return True
        except TimeoutException as err:
            Logger.error(f"Failed auth: {err}")
            return False
