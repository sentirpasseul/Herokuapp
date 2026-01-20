from conftest import browser
from elements.custom_elements.label import Label
from elements.custom_elements.web_element import WebElement


class UserCard(WebElement):
    USER_CARD = "(//div[contains(@class, 'figure')])[{index}]"
    ANY_USER_CARD = "(//div[contains(@class, 'figure')])"
    USERNAME = "//*[contains(text(), 'user{index}')]"
    LINK_PROFILE_ELEMENT = "//a[contains(@href, '/users/{index}')]"

    def __init__(self, browser, index: int = 1):
        locator = self.USER_CARD.format(index=index)
        description = f"User Card [{index}] -> User Card web element"
        super().__init__(browser, locator=locator, description=description)
        self.username = Label(browser=self.browser,
                              locator=self.USERNAME.format(index=index),
                              description=f"User Card [{index}] -> Username label")
        self.link_profile = Label(browser=self.browser,
                                  locator=self.LINK_PROFILE_ELEMENT.format(index=index),
                                  description=f"User Card [{index}] -> Link Profile label")

    def click_link_profile(self) -> None:
        self.link_profile.click()

    def get_username_text(self):
        return self.username.get_text()
