
from pages.practiceform_page import PracticeFormPage
from conftest import browser

def test_login_form_validate(browser):
    loginform_page = PracticeFormPage(browser)
    loginform_page.visit()
    assert loginform_page.user_email.get_dom_attribute('pattern') == 'name@example.com'
    loginform_page.user_email.send_keys(' ')
    assert loginform_page.btn_submit.click()
    assert not loginform_page()
