from pages.base_page import BasePage
from components.components import WebElement

class RadioButton(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)

        self.yes_radio = WebElement(driver, '#yesRadio')
        self.impressive_radio = WebElement(driver, '#impressiveRadio')
        self.no_radio = WebElement(driver, '#NoRadio')
        self.text = WebElement(driver, 'text')
