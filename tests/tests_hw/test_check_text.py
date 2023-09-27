from pages.demoqa_page import Demoqa
from pages.elements_page import ElementsPage
from conftest import browser

#1.	перейти на страницу 'https://demoqa.com/'
#b.	проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’

def test_page_footer(browser):
    demoqa_page = Demoqa(browser)
    demoqa_page.visit()
    assert (demoqa_page.element_footer_text.exist())

            #== Demoqa('© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'))

#a.	перейти на страницу 'https://demoqa.com/'
#b.	через кнопку перейти на страницу 'https://demoqa.com/elements'
#c.	проверить что текст по центру == 'Please select an item from left to start practice.'

def test_text_center(browser):
    demo_qa_page = Demoqa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.clik()
    assert elements_page.get_text() == 'Please select an item from left to start practice.'
#

