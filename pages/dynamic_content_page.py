from pages.base_page import BasePage
from elements.custom_elements.label import Label
from elements.custom_elements.web_element import WebElement
from selenium.common.exceptions import TimeoutException


class DynamicContentPage(BasePage):
    UNIQUE_LOC = "//div[contains(@class, 'example')]//*[contains(text(), 'Dynamic Content')]"
    IMAGES_LOC = "//*[@id='content']//img"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(browser=browser, locator=self.UNIQUE_LOC,
                                    description="Dynamic Content Page -> Dynamic Content label")
        self.image = WebElement(browser=self.browser,
                          locator=loc,
                          description=f"Image #{number}")


    def get_image(self, number: int = 1, indexed_locator: str = None):
        loc = indexed_locator if indexed_locator else self.IMAGES_LOC
        return WebElement(browser=self.browser,
                          locator=loc,
                          description=f"Image #{number}")

    def get_images(self):
        elements = self.get_image().wait_for_all_visible()
        images_containers = []

        for i in range(1, len(elements) + 1):
            indexed_path = f"({self.IMAGES_LOC})[{i}]"

            container_obj = self.get_image(number=i, indexed_locator=indexed_path)
            images_containers.append(container_obj)
        return images_containers

    def check_images_two_coincidence(self):
        try:
            images = self.get_images()
            images_src = [image.get_attribute('src') for image in images]
            pair_images = set()

            while True:
                for attribute in images_src:
                    if attribute in pair_images:
                        return True
                    pair_images.add(attribute)
                self.browser.refresh()

        except TimeoutException:
            return False
