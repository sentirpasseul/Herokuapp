from selenium.webdriver import ActionChains

from elements.custom_elements.input import Input
from utils.js.javascript_actions import JavaScriptActions


class HorizontalSlider(Input):

    def __init__(self, browser, locator, description):
        super().__init__(browser=browser, locator=locator, description=description)
        self.js_actions = JavaScriptActions(browser)

    def set_value_to_slider(self, value):
        element = self.wait_for_visible()
        self.js_actions.set_value_to_element(value=value, element=element)
        self.js_actions.dispatch_event_change(element)
