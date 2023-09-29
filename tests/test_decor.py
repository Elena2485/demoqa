
from conftest import browser
from pages.demoqa_page import Demoqa
from pages.radio_button import  RadioButton

@pytest.mark.skip
def test_decor_3(browser):
    demo = Demoqa(browser)
    demo.visit()

    assert demo.h5.check_count_elements(6)

    for element in demo.h5.find_elements():
        assert element.text != ''

@pytest.mark.skipif(True, reason='просто пропуск')

def test_decor_1(browser):
    radio = RadioButton(browser)
    radio.visit()

    radio.btn_yes_radio.click_force()
    assert radio.text.get_text() == 'Yes have selected Yes'

    radio.btn_impressive_radio.click_force()
    assert radio.text.get_text == 'You have selected Impressive'

    assert 'disabled' in radio.btn_no_radio.get_dom_attribute('class')


