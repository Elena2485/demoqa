
#from selenium.webdriver.common.by import By
from pages.demoqa_page import Demoqa

def test_icon_exist(browser):
    demo_qa_page = Demoqa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.exist()

#   icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')

    if demo_qa_page.icon is None:
        print('Элемент не найден')
    else:
        print('Элемент найден')

