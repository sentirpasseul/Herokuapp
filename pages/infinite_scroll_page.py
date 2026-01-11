from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from elements.custom_elements.container import Container
from elements.custom_elements.label import Label
from utils.logs.logger import Logger


class InfiniteScrollPage(BasePage):
    INFINITE_SCROLL_PAGE_UNIQUE_LOC = "//div[contains(@class,'example')]//*[contains(text(), 'Infinite Scroll')]"
    PARAGRAPH_LOC = "//div[contains(@class,'jscroll-inner')]//div[contains(@class, 'jscroll-added')]"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.INFINITE_SCROLL_PAGE_UNIQUE_LOC,
                                    description="Infinite Scroll Page -> Infinite Scroll label")

    def get_paragraph(self, number: int = None):
        locator = f"{self.PARAGRAPH_LOC}[{number}]" if number else self.PARAGRAPH_LOC
        return Container(browser=self.browser,
                         locator=locator,
                         description=f"Infinite Scroll Page -> Paragraph[{number if number else 'all'}]")

    def get_paragraphs(self):
        return self.get_paragraph().wait_for_all_visible()

    def check_quantity_paragraphs_to_engineer_age(self, age):
        try:
            current_count = 0
            while current_count < age:
                paragraphs = self.get_paragraphs()
                current_count = len(paragraphs)

                Logger.info(f"Найдено элементов: {current_count}, нужно: {age}")

                if current_count >= age:
                    break

                last_paragraph = paragraphs[-1]
                last_paragraph.is_displayed()
                self.browser.scroll_to_element(last_paragraph)

            return True
        except TimeoutException:
            return False
