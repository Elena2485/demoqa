
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement

class Demoqa(BasePage):
    #три строки во всех проектах
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.element_footer_text = WebElement(driver,'#app > footer >span')
        self.h5 = WebElement(driver, 'div > h5')
