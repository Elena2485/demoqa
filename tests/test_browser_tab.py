from pages.browser_tab import BrowserTab
import time
from conftest import browser

## три раза подумать прежде чем использовать эти методы !!!
def test_browser_tab(browser):
    browser_tab = BrowserTab(browser)
    browser_tab.visit()

    assert len(browser.window_handles) == 1
    browser_tab.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)