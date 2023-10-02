from conftest import browser
from pages.form_page import FormPage
import time
#def test_state(browser):
#    form_page = FormPage(browser)
#    time.sleep(2)
#   form_page.btn_state.scroll_to_element()
#    form_page.btn_state.click()
#   form_page.btn_NCR.click()
#    time.sleep(2)

def test_state_2(browser)
    form_page = FormPage(browser)
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.inp_state.send_keys('NCR')
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)