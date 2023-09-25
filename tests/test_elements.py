from pages.checkbox_page import Checkbox
from pages.elements_page import ElementsPage
from conftest import browser


def test_find_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()

    assert elements_page.btn_elements.check_count_elements(count= 9)
##########################
def test_count_checkbox(browser):
    check_page = Checkbox(browser)
    check_page.visit()

    assert check_page.chekbox.check_count_elements(1)
    check_page.btn_expand_all.click()
    assert check_page.chekbox.check_count_elements(17)
    browser.refresh()
    assert check_page.chekbox.check_count_elements(1)