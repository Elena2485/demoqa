from pages.demoqa_page import Demoqa
from pages.elements_page import ElementsPage

#1.	перейти на страницу 'https://demoqa.com/'
#b.	проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’

def test_page_footer(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.footer_text.get_text() == ('© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.')

#a.	перейти на страницу 'https://demoqa.com/'
#b.	через кнопку перейти на страницу 'https://demoqa.com/elements'
#c.	проверить что текст по центру == 'Please select an item from left to start practice.'

def test_text_center(browser):
    demo_qa_page = Demoqa(browser)
    elements_page = ElementsPage()
    demo_qa_page.visit()
    demo_qa_page.btn_elements.clik()
    assert elements_page.text_elements.get_text() == 'Please select an item from left to start practice.'
#

