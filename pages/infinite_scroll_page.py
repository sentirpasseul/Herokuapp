import pytest
from bs4 import BeautifulSoup

from pages.base_page import BasePage
from elements.custom_elements.web_element import WebElement
from elements.custom_elements.label import Label
from utils.logs.logger import Logger


class InfiniteScrollPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class,'example')]//*[contains(text(), 'Infinite Scroll')]"
    PARAGRAPH_LOC = "(//div[contains(@class,'jscroll-inner')]//div[contains(@class, 'jscroll-added')])[{index}]"
    TIMEOUT_PARAGRAPH = 3

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Infinite Scroll Page -> Infinite Scroll label")

    def get_paragraphs_count(self):
        html = self.browser.execute_script("return document.documentElement.outerHTML;")
        soup = BeautifulSoup(html, "html.parser")
        return len(soup.find_all('div', class_="jscroll-added"))

    def scroll_to_paragraph_by_index(self, index) -> None:
        paragraph = WebElement(browser=self.browser,
                               locator=self.PARAGRAPH_LOC.format(index=index),
                               description=f"Paragraph {index}",
                               timeout=self.TIMEOUT_PARAGRAPH)
        paragraph.wait_for_visible()
        paragraph.scroll_to_element()
