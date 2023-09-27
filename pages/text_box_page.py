from pages.base_page import BasePage
from components.components import WebElement

class TextBoxPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName')
        self.user_email = WebElement(driver, '#userEmail')
        self.current_address = WebElement(driver, '#currentAddress')
        self.state_city = WebElement(driver, '# stateCity')