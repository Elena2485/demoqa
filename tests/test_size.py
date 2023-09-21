
from pages.demoqa_page import Demoqa #единственный что сделала без ошибок
import time
def test_check_size(browser):
    demo_qa_page = Demoqa(browser)
    demoqa_page.visit()
    demo_qa_page.set_window_size(width=1000, height=300)
    time.sleep(2)
    demo_qa_page.set_window_size(width=1000, height=1000)