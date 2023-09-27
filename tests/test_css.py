
import time
from pages.elements_page import ElementsPage
from components.components import WebElement

def test_flex_menu(browser):
    element_page = ElementsPage(browser)
    element_page.visit()
    assert element_page.block_menu.check_css('flex', 0)

    assert element_page.style('max-width') == '25%'
    time.sleep(2)
    element_page.set_window_size(width=1000, height=1000)
    time.sleep(2)
    element_page.set_window_size(width=1000, height=1000)


    #новые значен