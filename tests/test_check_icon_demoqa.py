
#from selenium.webdriver.common.by import By
from conftest import browser
from pages.demoqa_page import Demoqa

def test_icon_exist(browser):
    demo_qa_page = Demoqa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.icon.exist()
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url()
