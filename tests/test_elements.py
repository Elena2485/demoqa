
from pages.elements_page import ElementsPage

def test_find_elements(browser):


   # btns_first_menu = 'div:nth-child(1) > div > ul > li'
    elements_page = Elements_page(browser)
    elements_page.visit()

    assert demo_qa_page.check_count_elements.btns(count= 9)
