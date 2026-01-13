from pages.base_page import BasePage
from elements.custom_elements.label import Label
from elements.custom_elements.web_element import WebElement
from elements.custom_elements.user_card import UserCard
from typing import List


class HoversPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Hovers')]"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Hovers Page -> Hovers label")
        self.user_card = WebElement(browser=browser,
                                    locator=UserCard.UNIQUE_LOC,
                                    description="Hovers Page -> User Card web element")
        self.driver = browser.driver

    @property
    def cards(self) -> List[UserCard]:
        user_card_elements = self.user_card.wait_for_all_visible()
        return [UserCard(self.browser, i + 1) for i in range(len(user_card_elements))]
