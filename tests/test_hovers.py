import pytest

from conftest import browser
from pages.hovers_page import HoversPage
from config.urls import URLs
from utils.markers.markers import critical


@critical
class TestHovers:
    def test_hovers_page(self, browser):
        browser.get(URLs.HOVERS_PAGE)
        hovers_page = HoversPage(browser=browser)

        hovers_page.wait_for_open()
        user_cards = hovers_page.cards
        for index in range(1, len(user_cards) + 1):
            hovers_page.hover_user_card(index)
            actual_text = hovers_page.get_username_of_user_card(index)
            assert isinstance(actual_text, str), (f"Ошибка при проверке типа {actual_text}\n"
                                                  f"Actual: {type(actual_text)} \n"
                                                  "Expected: str")
            assert f"user{index}" in actual_text, ("Ошибка при проверке имени пользователя \n"
                                                   f"Actual: user{index} in {actual_text} \n"
                                                   f"Expected: user{index} in {actual_text}")
            hovers_page.hover_user_card(index)
            hovers_page.click_link_profile_of_user_card(index)
            current_url = browser.current_url
            assert current_url == URLs.LINK_PROFILE.format(index=index), \
                ("Ошибка при проверке URL профиля \n"
                 f"Actual: {current_url} \n"
                 f"Expected: {URLs.LINK_PROFILE.format(index=index)}")
            browser.go_back()
