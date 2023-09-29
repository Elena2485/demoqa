from pages.text_box_page import TextBoxPage
from conftest import browser


def test_placeholder(browser):
    text_box_page = TextBoxPage(browser)
    text_box_page.visit()
    assert text_box_page.full_name.get_dom_attribute('placeholder') == 'Full Name'