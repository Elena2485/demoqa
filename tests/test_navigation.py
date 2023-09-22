
from pages.demoqa_page import Demoqa
from pages.elements_page import ElementsPage

def test_navigation(browser):
    demo_qa_page = Demoqa(browser)
    elements_page = ElementsPage()
    demo_qa_page.visit()
    demo_qa_page.btn_elements.clik()
    demo_qa_page.refresh()

 #   browser.back()
 #   browser.forward()
 #   ElementsPage.equal_url()

