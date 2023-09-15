#from conftest import browser
#from selenium.webdriver.common.by import By

from pages.demoqa import DemoQa
def test_icon_exist(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.click_on_the_icon()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_icon()

def equal_url(self):
    if self.get_url() == 'https://demoqa.com/':
       return True
    return False

def get_url(self):
    return self.driver.current_url
