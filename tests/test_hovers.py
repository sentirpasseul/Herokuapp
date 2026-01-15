from pages.hovers_page import HoversPage
from elements.custom_elements.user_card import UserCard
from config.urls import URLs


class TestHovers:
    def test_hovers_page(self, browser):
        browser.get(URLs.HOVERS_PAGE)
        hovers_page = HoversPage(browser=browser)

        hovers_page.wait_for_open()
        all_cards = hovers_page.cards
        for i, card in enumerate(all_cards, start=1):
            card.hover()
            actual_text = card.username.get_text()
            assert isinstance(actual_text, str), (f"Ошибка при проверке типа {actual_text}\n"
                                                  f"Actual: {type(actual_text)} \n"
                                                  "Expected: str")
            assert f"user{i}" in actual_text, ("Ошибка при проверке имени пользователя \n"
                                               f"Actual: user{i} in {actual_text} \n"
                                               f"Expected: user{i} in {actual_text}")
            card.hover()
            card.link_profile.click()
            current_url = hovers_page.get_current_url()
            assert current_url == UserCard.LINK_PROFILE.format(index=i), \
                ("Ошибка при проверке URL профиля \n"
                 f"Actual: {current_url} \n"
                 f"Expected: {UserCard.LINK_PROFILE.format(index=i)}")
            hovers_page.go_to_previous_page()
