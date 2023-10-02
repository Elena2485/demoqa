import pytest

from pages.demoqa_page import Demoqa
from pages.alerts import Alerts
from pages.accordion import Accordion
from pages.browser_tab import BrowserTab
from conftest import browser
import time

def test_check_title_demo(browser):
    demoqa_page = Demoqa(browser)
    demoqa_page.visit()
    assert browser.title == 'DEMOQA'

@pytest.Mark.parametrsize('pages', [Accordion, Alerts, Demoqa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visist()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'