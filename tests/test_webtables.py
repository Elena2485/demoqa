from pages.tables_page import Tables
from conftest import browser
import time
def test_tables(browser):
    page_tables = Tables(browser)
    page_tables.visit()


    assert not page_tables.no_data.exist()
 #   удаление всех записей

    while page_tables.btn
