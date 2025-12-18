from pages.base_page import BasePage
from utils.logs.logger import Logger
from pages.alerts_page import AlertsPage
from selenium.common.exceptions import TimeoutException


class ContextMenuPage(BasePage):
    CONTEXT_AREA_LOC = "hot-spot"
    CONTEXT_MENU_PAGE_UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Context Menu')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = self.element(locator=self.CONTEXT_MENU_PAGE_UNIQUE_LOC)
        self.alerts = AlertsPage(browser)

    def open(self):
        try:
            self.wait_for_open()
            return True
        except TimeoutException:
            return False

    def check_context_menu(self, text):
        try:
            context_area = self.element(locator=self.CONTEXT_AREA_LOC)
            context_area.wait_for_visible()
            context_area.move_mouse_to_div()
            context_area.right_click()
            self.browser.switch_to_alert()
            self.alerts.check_alert_text(text=text)
            self.browser.confirm_alert()
            Logger.info(f"Check {self.page_name} successfully!")
            return True
        except Exception as err:
            Logger.error(f"Failed to check context_menu: {err}")
            return False
