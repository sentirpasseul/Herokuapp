from pages.base_page import BasePage
from elements.custom_elements.label import Label
from selenium.common.exceptions import TimeoutException
from elements.custom_elements.container import Container
from typing import List


class HoversPage(BasePage):
    HOVERS_PAGE_UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Hovers')]"
    USER_CARD_LOC = "//div[contains(@class, 'figure')]"
    USER_CARD_USERNAME = "//*[contains(text(), 'user{user_id}')]"
    USER_CARD_LINK_PROFILE = "//a[contains(@href, '/users/{user_id}')]"
    USER_PROFILE_LINK = "https://the-internet.herokuapp.com/users/{user_id}"
    USER_CARD_TIMEOUT = 20

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser, locator=self.HOVERS_PAGE_UNIQUE_LOC,
                                    description="Hovers Page -> Hovers label")
        self.driver = browser.driver

    def open(self):
        try:
            self.wait_for_open()
            return True
        except TimeoutException:
            return False

    def get_user_card_username(self, user_id):
        dynamic_locator = self.USER_CARD_USERNAME.format(user_id=user_id)
        return Label(browser=self.browser,
                     locator=dynamic_locator,
                     description=f"Hovers Page -> Username[user{user_id}] of User Card label")

    def get_user_card_link_profile(self, user_id):
        dynamic_locator = self.USER_CARD_LINK_PROFILE.format(user_id=user_id)
        return Label(browser=self.browser,
                     locator=dynamic_locator,
                     description=f"Hovers Page -> User Card Profile on user{user_id}")

    def get_user_card(self):
        return Container(browser=self.browser,
                         locator=self.USER_CARD_LOC,
                         description="Hovers Page -> User Card container")

    def get_user_cards(self) -> List[Container]:
        cards = self.get_user_card().wait_for_all_visible()
        containers = []
        for i, element in enumerate(cards, start=1):
            indexed_locator = f"({self.USER_CARD_LOC})[{i}]"

            container_obj = Container(
                browser=self.browser,
                locator=indexed_locator,
                description=f"Hovers Page -> User Card container #{i}",
                timeout=self.USER_CARD_TIMEOUT
            )
            containers.append(container_obj)
        return containers

    def check_correct_url(self, url: str):
        return True if self.browser.current_url == url else False

    def check_user_cards(self):
        cards = self.get_user_cards()
        quantity_of_cards = len(cards)
        for user_id in range(quantity_of_cards):
            card = cards[user_id]
            username = self.get_user_card_username(user_id + 1)
            link_profile = self.get_user_card_link_profile(user_id + 1)

            card.wait_for_visible()
            card.move_mouse_to_div()

            username.wait_for_visible()
            link_profile.wait_for_visible()
            link_profile.click()
            self.check_correct_url(self.USER_PROFILE_LINK.format(user_id=user_id))
            self.browser.go_back()
