from pages.base_page import BasePage
from components.components import WebElement
class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text_please = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.btn_elements = WebElement(driver, 'div.playgound - header > div')

    #   def exist_icon(self):
    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False

#def test_go_to_page_elements():
#    demo_qa_page = Demoqa(browser)
#   elements_page = ElementsPages(browser)

#    demo_qa_page.visit()
 #   assert demo_qa_page.equal_url()
#    demo_qa_page.click_on_the_btn_elements()
 #   assert elements_page.equal_url()


