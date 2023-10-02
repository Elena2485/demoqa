from conftest import browser
import time
from pages.elements_page import ElementsPage

def test_flex_menu(browser):
    element_page = ElementsPage(browser)
    element_page.visit()
    assert element_page.block_menu.check_css('flex', '0 0 25%')
    assert element_page.block_menu.check_css('max-width', '25%')
    browser.set_window_size(320, 480)
    assert element_page.style('max-width') == '25%'
    time.sleep(2)
    element_page.set_window_size(width=1000, height=1000)
    time.sleep(2)
    element_page.set_window_size(width=1000, height=1000)

###



    el_page.visit()
    assert el_page.block_menu.check_css('flex', '0 0 25%')
    assert el_page.block_menu.check_css('max-width', '25%')
    browser.set_window_size(320, 480)
    assert el_page.block_menu.check_css('flex', '0 0 100%')
    assert el_page.block_menu.check_css('max-width', '100%')
    browser.set_window_size(1000, 1000)
