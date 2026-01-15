from conftest import browser
from elements.custom_elements.label import Label
from elements.custom_elements.web_element import WebElement
from elements.base_element import BaseElement


class UserCard(BaseElement):
    USER_CARD = "(//div[contains(@class, 'figure')])[{index}]"
    ANY_USER_CARD = "(//div[contains(@class, 'figure')])"
    USERNAME = "//*[contains(text(), 'user{index}')]"
    LINK_PROFILE_ELEMENT = "//a[contains(@href, '/users/{index}')]"
    LINK_PROFILE = "https://the-internet.herokuapp.com/users/{index}"

    def __init__(self, browser, index):
        super().__init__(browser)
        self.user_card = WebElement(browser=self.browser,
                                    locator=self.USER_CARD.format(index=index),
                                    description=f"User Card [{index}] -> User Card web element")
        self.username = Label(browser=self.browser,
                              locator=self.USERNAME.format(index=index),
                              description=f"User Card [{index}] -> Username label")
        self.link_profile = Label(browser=self.browser,
                                  locator=self.LINK_PROFILE_ELEMENT.format(index=index),
                                  description=f"User Card [{index}] -> Link Profile label"  )

    def hover(self) -> None:
        self.user_card.move_mouse_to_element()
