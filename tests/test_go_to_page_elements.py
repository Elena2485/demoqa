from pages.demoqa_page import Demoqa
from pages.elements_page import ElementsPage

def test_go_page_elements(browser):
    demo_qa_page = Demoqa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.icon.click()
 #  demo_qa_page.click_on_the_btn_elements()
    assert elements_page.equal_url()





