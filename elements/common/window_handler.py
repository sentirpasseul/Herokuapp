from core.browser import Browser


class WindowHandler:
    def __init__(self, browser: Browser):
        self.browser = browser

    def open_new_tab(self) -> None:
        self.browser.switch_to_new_tab()

    def return_to_main_tab(self) -> None:
        self.browser.switch_to_original_window()

    def close_extra_tabs(self):
        handles = self.browser.driver.window_handles
        for handle in handles[1:]:
            self.browser.driver.switch_to.window(handle)
            self.browser.driver.close()
        self.return_to_main_tab()

    def go_back(self) -> None:
        self.browser.go_back()

    def refresh(self) -> None:
        self.browser.refresh()
