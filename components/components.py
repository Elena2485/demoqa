
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException #исключения прописываем, чтобы можно было вылавливать..
from selenium.webdriver.common.keys import Keys

class WebElement:
    def __init__(self, driver, locator='', locator_type = 'css', head_meta = 'head > meta'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type
        self.head_meta = head_meta

    def click(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator).click()

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.locator)

    def exist(self):
        try:
            self.driver.find_element()
        except NoSuchElementException:
            return False
        return True

    def exist_icon(self):
        try:
            #self.icon.find_element()
            self.driver.find_element()
        except NoSuchElementException:
            return False
        return True

    def visible(self):
        return self.driver.find_element.is_displayed()

    #######################
    def not_visible(self):
        return self.driver.find_element.btn_sidebar_first_checkbox()

    #################
    def check_count_elements(self, count: int) -> bool:
        if len(self.find_element()) == count:
            return True
        return False
    ######################
    def send_keys(self, text: str):
        return self.find_element().send_keys(text)

    def click_force(self):
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def clear(self):
        self.find_element().send_keys(Keys.CONTROL + 'a')
        self.find_element().send_keys(Keys.DELETE)
        self.find_element().send_keys(Keys.ARROW_DOWN)
        self.find_element().send_keys(Keys.ENTER)


    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    def scroll_to_element(self):
        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);',
            self.find_element()
        )

    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        elif self.locator_type == 'name':
            return By.NAME
        elif self.locator_type == 'xpath':
            return By.XPATH
        elif self.locator_type == 'css':
            return By.CSS_SELECTOR
        elif self.locator_type == 'class':
            return By.CLASS_NAME
        elif self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print('Locator type ' + (self.locator_type) + ' not correct')

    def check_css(self, style, value= ''):
        return self.find_element().value_of_css_property(style) == value

