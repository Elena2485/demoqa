from pages.demoqa_page import Demoqa
from pages.elements_page import ElementsPage

def test_find_elements(browser):


   # btns_first_menu = 'div:nth-child(1) > div > ul > li'
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert demoqa_page.check_count_elements.btns(count= 9)
