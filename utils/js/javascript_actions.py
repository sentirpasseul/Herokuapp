from core.browser import Browser
from utils.logs.logger import Logger


class JavaScriptActions:

    def __init__(self, browser: Browser):
        self.browser = browser

    def set_value_to_element(self, value, element):
        self.browser.execute_script("arguments[0].value=arguments[1]", element, value)

    def dispatch_event_change(self, element):
        self.browser.execute_script("arguments[0].dispatchEvent(new Event('change',{ bubbles: true }))", element)
