from pages.elements_page import ElementsPage
import time

def test_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
  #  elements_page.test_btn_first_textbox()
  #  elements_page.icon.click()
    # time sleep(3)
    # assert elements_page.btn_sidebar_first_textbox.exist()
    assert elements_page.btn_sidebar_first_textbox.visible()

def test_not_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btn_sidebar_first_checkbox.visible()
    elements_page.btn_sidebar_first_click()
    time.sleep(2)
    assert not (elements_page.btn_sidebar.visible_first_checkbox.visible()

                #== 'div:nth-child(1) > div > ul > #item-1 > span')

