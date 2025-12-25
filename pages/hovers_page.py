from pages.base_page import BasePage
from elements.custom_elements.label import Label
from selenium.common.exceptions import TimeoutException
from elements.custom_elements.container import Container
from typing import List


class HoversPage(BasePage):
    HOVERS_PAGE_UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Hovers')]"
    USER_CARD = "//div[contains(@class, 'figure')]"
    USER_CARD_USERNAME = "//*[contains(text(), 'user{id}')]"
    USER_CARD_LINK_PROFILE = "//a[contains(@href, '/users/{id}')]"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser, locator=self.HOVERS_PAGE_UNIQUE_LOC,
                                    description="Hovers Page -> Hovers label")

    def open(self):
        try:
            self.wait_for_open()
            return True
        except TimeoutException:
            return False

    def get_user_card_username(self, id):
        dynamic_locator = self.USER_CARD_USERNAME.format(id=id)
        return Label(browser=self.browser,
                     locator=dynamic_locator,
                     description=f"Hovers Page -> Username[user{id}] of User Card label")

    def get_user_card_link_profile(self, id):
        dynamic_locator = self.USER_CARD_LINK_PROFILE.format(id=id)
        return Label(browser=self.browser,
                     locator=dynamic_locator,
                     description=f"Hovers Page -> User Card Profile on user{id}")

    def get_user_card(self):
        return Container(browser=self.browser,
                         locator=self.USER_CARD,
                         description="Hovers Page -> User Card container")

    def get_user_cards(self) -> List[Container]:
        cards = self.get_user_card().wait_for_all_visible()
        containers = []
        for i, element in enumerate(cards, start=1):
            indexed_locator = f"({self.USER_CARD})[{i}]"

            container_obj = Container(
                browser=self.browser,
                locator=indexed_locator,
                description=f"Hovers Page -> User Card container #{i}"
            )
            containers.append(container_obj)
        return containers

    def check_user_cards(self):
        cards = self.get_user_cards()
        quantity_of_cards = len(cards)
        for user_id in range(quantity_of_cards):
            card = cards[user_id]
            username = self.get_user_card_username(user_id)
            link_profile = self.get_user_card_link_profile(user_id)
            card.wait_for_visible()
            card.move_mouse_to_div()
