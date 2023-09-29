#from selenium.webdriver.common.by import By

import  logging
import requests

class BasePage:
    def __init__(self, driver, base_url, metaView):
        self.driver = driver
        self.base_url = base_url  #'https://demoqa.com/'
        self.metaView = metaView
    def visit(self):
        return self.driver.get(self.base_url)
    def back(self):
        return self.driver.back

    def forward(self):
        return self.driver.forward()

    def refresh(self):
        return self.driver.refresh()

#    def find_element(self, locator):   перенесен в class WebElement
#        time.sleep(3) #задержка на 3 секунды
#       return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def equal_url(self): # используется в дочерних
        if self.get_url() == self.base_url:
            return True
        return False

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False


    def code_status(self):
        resp = requests.get(self.base_url)
        return resp.status_code == 200