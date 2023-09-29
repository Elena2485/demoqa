
from pages.alerts import Alerts
from conftest import browser
import time

def test_allert(browser):
    alert_page = Alerts(browser)
    alert_page.visit()

    assert not alert_page.alert()

    alert_page.alertButton.click()
    time.sleep(2)
    assert alert_page.alert()
    alert_page.alert().accept()

def test_alert_text(browser):
    alert_page = Alerts(browser)
    alert_page.visit()

    alert_page.alertButton.click()
    assert alert_page.alert().text == 'You clicked'

def test_confirm(browser):
    alert_page = Alerts(browser)
    alert_page.visit()

    alert_page.confirmButton().click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.confirmResult.get_text() == 'You selected Cancel'

def test_promt(browser):
    alert_page = Alerts(browser)
    alert_page.visit()

    alert_page.promtButton().click()
    time.sleep(2)
    alert_page.alert().send_keys('Elena')
    alert_page.alert().accept()
    assert alert_page.promptResult.get_text() == 'You entered Elena'
    time.sleep(2)