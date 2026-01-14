from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from elements.custom_elements.web_element import WebElement
from elements.custom_elements.label import Label
from utils.logs.logger import Logger


class InfiniteScrollPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class,'example')]//*[contains(text(), 'Infinite Scroll')]"
    PARAGRAPH_LOC = "//div[contains(@class,'jscroll-inner')]//div[contains(@class, 'jscroll-added')]"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Infinite Scroll Page -> Infinite Scroll label")
        self.paragraph = WebElement(browser=self.browser,
                                    locator=self.PARAGRAPH_LOC,
                                    description=f"Infinite Scroll Page -> Paragraph")

    def get_paragraphs(self):
        return self.paragraph.wait_for_all_visible()

    def scroll_page_to_element(self, element) -> None:
        self.browser.scroll_to_element(element)
