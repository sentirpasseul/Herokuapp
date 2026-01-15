from core.browser import Browser
from utils.logs.logger import Logger


class BasePage:

    def __init__(self, browser: Browser):
        self.browser = browser
        self.page_name = None
        self.unique_element = None

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.page_name}]"

    def __repr__(self) -> str:
        return str(self)

    def wait_for_open(self):
        Logger.info(f"{self}: wait for open")
        self.unique_element.wait_for_presence()

    def refresh_page(self) -> None:
        self.browser.refresh()

    def go_to_previous_page(self) -> None:
        self.browser.go_back()

    def get_new_window_title(self):
        return self.browser.get_title()

    def open_new_tab(self) -> None:
        self.browser.switch_to_new_tab()

    def return_to_main_tab(self) -> None:
        self.browser.switch_to_original_window()

    def close_extra_tabs(self) -> None:
        handles = self.browser.driver.window_handles
        for handle in handles[1:]:
            self.browser.driver.switch_to.window(handle)
            self.browser.driver.close()
        self.return_to_main_tab()
