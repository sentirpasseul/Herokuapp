from pages.base_page import BasePage
from utils.logs.logger import Logger
from pages.alerts_page import AlertsPage


class ContextMenuPage(BasePage):

    CONTEXT_MENU_PAGE_LINK = "http://the-internet.herokuapp.com/context_menu"
    CONTEXT_AREA_LOC = "//*[@*='hot-spot']"

    def __init__(self, browser, text):
        super().__init__(browser)
        self.unique_element = self.element(locator="//div[contains(@class, 'example')]//*[contains(text(), 'Context Menu')]",
                                           browser=self.browser)
        self.alerts = AlertsPage(browser)
        self.text = text


    def open(self):
        try:
            self.browser.get(self.CONTEXT_MENU_PAGE_LINK)
            self.wait_for_open()
            return True
        except Exception as err:
            return False

    def check_context_menu(self):
        try:
            context_area = self.element (locator=self.CONTEXT_AREA_LOC,
                                         browser=self.browser)
            context_area.move_mouse_to_div()
            context_area.right_click()
            self.browser.switch_to_alert()
            self.alerts.check_alert_text(text=self.text)
            self.browser.confirm_alert()
            Logger.info(f"Check context menu successfully!")
            return True
        except Exception as err:
            Logger.error(f"Failed to check context_menu: {err}")
            return False

