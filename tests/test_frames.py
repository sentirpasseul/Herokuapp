from pages.frames_page import FramePage
from config.urls import URLs


class TestFrames:
    def test_frames_page(self, browser):
        browser.get(URLs.FRAMES_PAGE)
        frames_page = FramePage(browser)

        frames_page.wait_for_open()
        if not frames_page.is_menu_visible():
            frames_page.click_menu()

        frames_page.click_menu_item()
        browser.switch_to_frame(frames_page.nested_frames_page.iframe)
        assert frames_page.is_parent_frame_text_visible(), "Ошибка при проверке видимости родительского фрейма"
        browser.switch_to_frame(frames_page.nested_frames_page.iframe_child)
        assert frames_page.nested_frames_page.child_frame_text.wait_for_visible(), \
            "Ошибка при проверке видимости фрейма наследника"
