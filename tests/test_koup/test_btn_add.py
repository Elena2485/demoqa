from components.components import WebElement
from pages.koup import koup
from pages.koup_add import KoupAdd

def test_koup_add(browser):
    koup = koup(browser)
    koup_add  = KoupAdd(browser)
    koup.visit()
    assert koup.link_add.get_text() == 'Add/Remove Elememts'
    koup.link_add.click()
    assert koup_add.equal_url()

    assert koup_add.btn_add.get_text() == 'Add Element'

    assert koup_add.btn_add.get_dom_attribute('onclick') == 'addElement()'

#  неверное решение
#   assert test_koup_add.btns_delete.get_text() == 'Delete'

## when Кликнуть на кнопку 4 раза
#   for i in range(4):
 #       koup_add.btn_add.click()

#    assert koup_add.btns_delete.check_count_elements(4)

    # проверка для всех элементов
#    for element in koup_add_page.btns_delete.find_elements()
#  When Кликнуть на каждую кнопку Delete""
# while koup_add.btns_delete.exist():
#     koup_add.btns_delete.click()
# assert not koup_add.btns_delete.exist()






