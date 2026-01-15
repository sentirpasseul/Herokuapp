from pages.base_page import BasePage
from elements.custom_elements.web_element import WebElement
from elements.custom_elements.label import Label
from typing import List


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

    def get_paragraphs(self) -> List[WebElement]:
        elements = self.paragraph.wait_for_all_visible()
        return [
            WebElement(browser=self.browser,
                       locator=f"({self.PARAGRAPH_LOC})[{i + 1}]",
                       description=f"Paragraph {i + 1}"
                       )
            for i in range(len(elements))
        ]

    def scroll_page_to_paragraph(self) -> None:
        self.paragraph.scroll_to_element()
