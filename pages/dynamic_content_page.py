from pages.base_page import BasePage
from elements.custom_elements.label import Label
from elements.custom_elements.multi_web_element import MultiWebElement


class DynamicContentPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Dynamic Content')]"
    IMAGES_LOC = "(//*[@id='content']//img)[{index}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser=browser, locator=self.UNIQUE_LOC,
                                    description="Dynamic Content Page -> Dynamic Content label")
        self.images = MultiWebElement(browser=self.browser,
                                      formatable_xpath=self.IMAGES_LOC,
                                      description=f"Images")

    def get_all_src(self):
        return [image.get_attribute("src") for image in self.images]
