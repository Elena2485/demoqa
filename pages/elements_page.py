from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.get_text = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.btn_elements = WebElement(driver, 'div.playgound - header > div')
        self.text_elements = WebElement(driver, '')


    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False



