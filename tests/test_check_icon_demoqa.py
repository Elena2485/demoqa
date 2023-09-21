
#from selenium.webdriver.common.by import By

from pages.demoqa import Demoqa

def test_icon_exist(browser):
 #   browser.get('https://demoqa.com/')
    demo_qa_page = Demoqa(browser)
    demo_qa_page.visit()
    demo_qa_page.click_on_the_icon()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_icon()

#    icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')

    if icon is None:
        print('Элемент не найден')
    else:
        print('Элемент найден')

#def test_icon_exist(browser):
#    demo_qa_page = Demoqa(browser)
 #   demo_qa_page.visit()
##    assert demo_qa_page.equal_url()
#    demo_qa_page.btn_elements.click()
 #   assert demo_qa_page.exist_icon()
#    assert elements_page.equal_url()

#    assert demo_qa_page.exist_icon()

#def equal_url(self):
#   if self.get_url() == 'https://demoqa.com/':
#       return True
 #   return False

#def get_url(self):
#    return self.driver.current_url
