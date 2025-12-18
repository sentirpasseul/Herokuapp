from pages.base_page import BasePage
from utils.logs.logger import Logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class AuthPage(BasePage):
    AUTH_PAGE_UNIQUE_LOC = "//*[contains(text(), 'Basic Auth')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = self.element(locator=self.AUTH_PAGE_UNIQUE_LOC)

    def auth(self, user: str, password: str) -> None:
        try:
            self.browser.get(f"https://{user}:{password}@the-internet.herokuapp.com/basic_auth")
            Logger.info(f"{self}: process of authorization")
        except TimeoutException as err:
            Logger.error(f"{err}: cannot authorize on {self.page_name}")

    def is_auth_success(self):
        try:
            success_message = self.element(
                locator='//p[contains(text(), "Congratulations! You must have the proper credentials.")]')
            success_message.wait_for_visible()
            Logger.info(f"{self.page_name} successful")
            return True
        except TimeoutException as err:
            Logger.error(f"Failed auth {self.page_name}: {err}")
            return False
