from conftest import browser
from pages.elements_page import ElementsPage
from pages.demoqa_page import Demoqa

def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    demo_qa = Demoqa(browser)

    elements_page.visit()
    assert elements_page.text_elements.get_text() == 'Elements'



