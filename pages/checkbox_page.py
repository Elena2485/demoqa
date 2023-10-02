from pages.base_page import BasePage
from components.components import WebElement

class Checkbox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/checkbox'
        super().__init__(driver, self.base_url)

        self.checkbox_all = WebElement(driver, 'span.rct-text')
        self.btn_plus = WebElement(driver, '.rct-icon-expand-all')

