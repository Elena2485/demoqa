
from pages.demoqa_page import Demoqa

def test_check_title_demo(browser):
    demo_qa_page = Demoqa(browser)
    demoqa_page.visit()
    assert browser.title == 'DEMOQA'

