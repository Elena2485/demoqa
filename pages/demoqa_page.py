
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement
import time

class Demoqa(BasePage):
    #три строки во всех проектах
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.element_footer_text = WebElement(driver,'© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.')
    def web_elements(self, driver, locator):
        self.icon = WebElement(driver)
        self.btn_elements = WebElement(locator)
        self.element_footer_text = WebElement(locator)

##  def equal_url(self): (убираем в родительский класс)
##        if self.get_url() == 'https://demoqa.com/': (заменяем на строка ниже)
##       if self.get_url() == self.base_url:
##            return True
##       return False

