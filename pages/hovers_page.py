from pages.base_page import BasePage
from elements.custom_elements.label import Label
from selenium.common.exceptions import TimeoutException
from elements.custom_elements.web_element import WebElement
from typing import List


class HoversPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Hovers')]"
    USER_CARD_LOC = "//div[contains(@class, 'figure')]"
    USER_CARD_USERNAME = "//*[contains(text(), 'user{user_id}')]"
    USER_CARD_LINK_PROFILE = "//a[contains(@href, '/users/{user_id}')]"
    USER_PROFILE_LINK = "https://the-internet.herokuapp.com/users/{user_id}"
    USER_CARD_TIMEOUT = 20

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.unique_element = Label(browser=browser,
                                    locator=self.UNIQUE_LOC,
                                    description="Hovers Page -> Hovers label")
        self.driver = browser.driver
        self.user_card_username = Label(browser=self.browser,
                     locator=dynamic_locator,
                     description=f"Hovers Page -> Username[user{user_id}] of User Card label")
        self.user_card_link_profile = Label(browser=self.browser,
                     locator=dynamic_locator,
                     description=f"Hovers Page -> User Card Profile on user{user_id}")
        self.user_card = WebElement(browser=self.browser,
                          locator=self.USER_CARD_LOC,
                          description="Hovers Page -> User Card container")

    def _get_user_card_username(self, user_id):
        dynamic_locator = self.USER_CARD_USERNAME.format(user_id=user_id)
        return Label(browser=self.browser,
                     locator=dynamic_locator,
                     description=f"Hovers Page -> Username[user{user_id}] of User Card label")

    def _get_user_card_link_profile(self, user_id):
        dynamic_locator = self.USER_CARD_LINK_PROFILE.format(user_id=user_id)
        return Label(browser=self.browser,
                     locator=dynamic_locator,
                     description=f"Hovers Page -> User Card Profile on user{user_id}")

    def _get_user_card(self):
        return WebElement(browser=self.browser,
                          locator=self.USER_CARD_LOC,
                          description="Hovers Page -> User Card container")

    def get_user_cards(self) -> List[WebElement]:
        cards = self._get_user_card().wait_for_all_visible()
        containers = []
        for i, element in enumerate(cards, start=1):
            indexed_locator = f"({self.USER_CARD_LOC})[{i}]"

            container_obj = WebElement(
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
            username = self._get_user_card_username(user_id + 1)
            link_profile = self._get_user_card_link_profile(user_id + 1)

            card.wait_for_visible()
            card.move_mouse_to_div()

            username.wait_for_visible()
            link_profile.wait_for_visible()
            link_profile.click()
            self.check_correct_url(self.USER_PROFILE_LINK.format(user_id=user_id))
            self.browser.go_back()
