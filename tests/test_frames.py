from pages.frames_page import FramePage
from elements.custom_elements.frame import Frame
from config.urls import URLs


class TestFrames:
    def test_frames_page(self, browser):
        browser.get(URLs.FRAMES_PAGE)
        frames_page = FramePage(browser)

        frames_page.wait_for_open()
        if not frames_page.is_menu_visible():
            frames_page.click_menu()

        frames_page.menu_item_click()
        frames_page.nested_frames_page.switch_to_frame()
        assert frames_page.is_parent_frame_text_visible(), "Ошибка при проверке видимости родительского фрейма"
        frames_page.nested_frames_page.switch_to_child_frame()
        assert frames_page.nested_frames_page.child_frame_text.wait_for_visible(), "Ошибка при проверке видимости фрейма наследника"



