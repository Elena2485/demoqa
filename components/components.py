
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException #исключения прописываем, чтобы можно было вылавливать..

class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
       self.find_element().click()

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self, locator):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)
    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def exist_icon(self):
        try:
            self.icon.find_element()
        except NoSuchElementException:
            return False
        return True

    def visible(self):
        return self.find_element.is_displayed()

    #######################
    def not_visible(self):
        return self.find_element.btn_sidebar_first_checkbox()

    #################
    def check_count_elements(self, count: int) -> bool:
        if len(self.find_element()) == count:
            return True
        return False