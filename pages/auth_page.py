from base_page import BasePage
from utils.logs.logger import Logger
from selenium.common.exceptions import TimeoutException
from elements.base_element import BaseElement

class AuthPage(BasePage):

    def __init__(self):
        super().__init__(self.browser)
        self.alert = None
        self.alert_text = str


    def get_alert(self):
        try:
            self.alert = self.browser.switch_to_alert()
            self.alert_text = self.browser.get_alert_text()
        except TimeoutException as err:
            Logger.error(f"{err}: cannot get alert {self}")

    def auth(self, login: str, password: str):
        try:
            Logger.info(f"{self}: process of authorization")

        except TimeoutException as err:
            Logger.error(f"{err}: cannot authorize")