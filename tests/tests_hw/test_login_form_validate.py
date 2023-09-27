
from pages.practiceform_page import PracticeFormPage

def test_login_form_validate(browser):
    loginform_page = PracticeFormPage(browser)
    loginform_page.visit()
    assert loginform_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'