from enum import StrEnum


class URLs(StrEnum):
    BASE_URL = "http://the-internet.herokuapp.com"
    BASIC_AUTH_URL = "the-internet.herokuapp.com/basic_auth"
    AUTH_PAGE = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
    ALERTS_PAGE = "https://the-internet.herokuapp.com/javascript_alerts"
    CONTEXT_MENU_PAGE = "http://the-internet.herokuapp.com/context_menu"
    HORIZONTAL_SLIDER_PAGE = "http://the-internet.herokuapp.com/horizontal_slider"
    HOVERS_PAGE = "http://the-internet.herokuapp.com/hovers"
    LINK_PROFILE = "https://the-internet.herokuapp.com/users/{index}"
    WINDOWS_PAGE = "http://the-internet.herokuapp.com/windows"
    FRAMES_PAGE = "https://demoqa.com/frames"
    DYNAMIC_CONTENT_PAGE = "http://the-internet.herokuapp.com/dynamic_content"
    INFINITE_SCROLL_PAGE = "http://the-internet.herokuapp.com/infinite_scroll"
    UPLOAD_IMAGE_PAGE = "http://the-internet.herokuapp.com/upload"
