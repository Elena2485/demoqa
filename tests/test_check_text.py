from pages.elements_page import ElementsPage
from

def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.text_elements.get_text() == 'Elements'


