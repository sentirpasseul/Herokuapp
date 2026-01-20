from pages.base_page import BasePage
from elements.custom_elements.label import Label
from elements.custom_elements.multi_web_element import MultiWebElement
from elements.custom_elements.user_card import UserCard
from typing import List


class HoversPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Hovers')]"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Hovers Page -> Hovers label")
        self.user_card_collection = MultiWebElement(browser=browser,
                                                    locator=UserCard.ANY_USER_CARD,
                                                    description="Hovers Page -> User Card web element")

    @property
    def cards(self):
        user_card_elements = self.user_card_collection.wait_for_all_visible()
        return [UserCard(self.browser, i + 1) for i in range(len(user_card_elements))]

    def hover_user_card(self, index: int) -> None:
        card = UserCard(self.browser, index)
        card.move_mouse_to_element()

    def get_username_of_user_card(self, index: int):
        card = UserCard(self.browser, index)
        return card.get_username_text()

    def click_link_profile_of_user_card(self, index: int) -> None:
        card = UserCard(self.browser, index)
        card.click_link_profile()
