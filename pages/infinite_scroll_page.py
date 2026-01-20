from pages.base_page import BasePage
from elements.custom_elements.web_element import WebElement
from elements.custom_elements.multi_web_element import MultiWebElement
from elements.custom_elements.label import Label


class InfiniteScrollPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class,'example')]//*[contains(text(), 'Infinite Scroll')]"
    PARAGRAPH_LOC = "//div[contains(@class,'jscroll-inner')]//div[contains(@class, 'jscroll-added')]"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Infinite Scroll Page -> Infinite Scroll label")
        self.paragraphs = MultiWebElement(browser=self.browser,
                                          locator=self.PARAGRAPH_LOC,
                                          description="Infinite Scroll Page -> Paragraphs")

    def get_paragraphs_count(self):
        return len(self.paragraphs.wait_for_all_visible())

    def scroll_to_paragraph_by_index(self, index) -> None:
        paragraph = WebElement(browser=self.browser,
                               locator=f"({self.PARAGRAPH_LOC})[{index}]",
                               description=f"Paragraph {index}")
        paragraph.scroll_to_element()

    def is_paragraph_exists(self, index):
        paragraph = WebElement(
            browser=self.browser,
            locator=f"({self.PARAGRAPH_LOC})[{index}]",
            description=f"Check existence of paragraph {index}"
        )
        return paragraph.is_exists()
