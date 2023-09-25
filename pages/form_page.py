from pages.base_page import BasePage
from components.components import WebElement

class FormPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#user_email')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#body > div.fade.modal.show > div')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeMadal')
        self.hobbies = WebElement(driver, '#hobbies-chekbox-1')
        self.current_address = WebElement(driver, '#currentAddress')
        self.state_city = WebElement(driver, '#stateCity')

