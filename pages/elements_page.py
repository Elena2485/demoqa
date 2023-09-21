from pages.demoqa import Demoqa
#from pages.elements_page import ElementsPages

def test_go_to_page_elements():
    demo_qa_page = Demoqa(browser)
    elements_page = ElementsPages(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.click_on_the_btn_elements()
    assert elements_page.equal_url()


