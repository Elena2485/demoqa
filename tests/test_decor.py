
from conftest import browser
from pages.demoqa_page import Demoqa
from pages.radio_button import RadioButton
import pytest
# @pytest.mark.skip
def test_decor_3(browser):
    demo = Demoqa(browser)
    demo.visit()

    assert demo.h5.check_count_elements(6)

    for element in demo.h5.find_elements():
        assert element.text != ''

#@pytest.mark.skipif(True, reason='просто пропуск')

def test_decor_1(browser):
    radio = RadioButton(browser)
    if not radio.code_status():
        pytest.skip(reason=f'Страница {radio.base_url} недоступна')

    radio.visit()
    radio.yes_radio.click_force()
    assert radio.text.get_text() == 'Yes have selected Yes'

    radio.impressive_radio.click_force()
    assert radio.text.get_text == 'You have selected Impressive'

    assert 'disabled' in radio.no_radio.get_dom_attribute('class')






