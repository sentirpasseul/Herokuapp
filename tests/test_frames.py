from pages.frames_page import FramePage
from config.urls import URLs


class TestFrames:
    def test_frames_page(self, browser):
        browser.get(URLs.FRAMES_PAGE)
        frames_page = FramePage(browser)
        assert frames_page.open(), "Ошибка при открытии страницы Frames Page"
        assert frames_page.check_collapse_menu(), "Ошибка при проверке бокового меню"
        assert frames_page.nested_frames_page.check_parent_iframe(), "Ошибка при проверке iframe Parent"
        assert frames_page.nested_frames_page.check_child_iframe(), "Ошибка при проверке iframe Child"
