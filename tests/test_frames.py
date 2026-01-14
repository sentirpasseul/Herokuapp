from pages.frames_page import FramePage
from elements.custom_elements.frame import Frame
from config.urls import URLs


class TestFrames:
    def test_frames_page(self, browser):
        browser.get(URLs.FRAMES_PAGE)
        frames_page = FramePage(browser)
        frame = Frame(browser)

        frames_page.wait_for_open()
        if frames_page.menu.wait_for_element_not_visible():
            frames_page.click_menu()

        frames_page.menu_item_click()
        frame.switch_to_frame(frames_page.nested_frames_page.iframe)
        frames_page.nested_frames_page.parent_frame_text.wait_for_visible()
        frame.switch_to_frame(frames_page.nested_frames_page.iframe_child)
        frames_page.nested_frames_page.child_frame_text.wait_for_visible()



