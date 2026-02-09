from pages.base_page import BasePage
from elements.custom_elements.web_element import WebElement
from elements.custom_elements.multi_web_element import MultiWebElement
from elements.custom_elements.label import Label


class InfiniteScrollPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class,'example')]//*[contains(text(), 'Infinite Scroll')]"
    PARAGRAPH_LOC = "(//div[contains(@class,'jscroll-inner')]//div[contains(@class, 'jscroll-added')])[{index}]"
    TIMEOUT_PARAGRAPH = 4

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Infinite Scroll Page -> Infinite Scroll label")
        self.paragraphs = MultiWebElement(browser=self.browser,
                                          formatable_xpath=self.PARAGRAPH_LOC,
                                          description="Infinite Scroll Page -> Paragraphs",
                                          timeout=self.TIMEOUT_PARAGRAPH)

    def get_paragraphs_count(self):
        return len(self.get_paragraphs())

    def get_paragraphs(self):
        return [WebElement(self.browser, timeout=self.TIMEOUT_PARAGRAPH) for _ in self.paragraphs]

    def scroll_to_paragraph_by_index(self, index) -> None:
        paragraph = WebElement(browser=self.browser,
                               locator=self.PARAGRAPH_LOC.format(index=index),
                               description=f"Paragraph {index}")
        paragraph.scroll_to_element()
        paragraph.wait_for_visible()
