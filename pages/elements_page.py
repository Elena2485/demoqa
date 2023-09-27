from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.get_text = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.btn_elements = WebElement(driver, 'div.playgound - header > div')
        self.nav_bar = WebElement(driver, 'div > nav')
        self.btn_sidebar_first = WebElement(driver, '')
        self.btn_sidebar_first_textbox = WebElement(driver, '')
        self.text_elements = WebElement(driver, '')
        self.btn_sidebar = WebElement('')
        self.glock_menu = WebElement(driver, 'div.row > div:nth-child(1)')

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False



