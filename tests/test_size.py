from pages.elements_page import ElementsPage
from pages.demoqa_page import Demoqa
import time
def test_check_size(browser):
    demo_qa_page = Demoqa(browser)
    demo_qa_page.visit()
    demo_qa_page.set_window_size(width=1000, height=300)
    time.sleep(2)
    demo_qa_page.set_window_size(width=1000, height=1000)

#################
def test_visible_nav_bar(browser):
    elements = ElementsPage(browser)
    elements.visit()
    assert not elements.nav_bar.visible()
    browser.set_window_size(767, 1000)
    assert elements.nav_bar.visible()

########################


