"""
These tests cover BARCO ClickShare Warranty Info.
"""

from pages.warranty_info import WarrantyPage

def test_warranty(browser):
    warranty_page = WarrantyPage(browser)
    serial_number = '1863552437'

    # ==Given== `Check your ClickShare warranty` page is displayed
    warranty_page.load()
    # ==When== User input `serial number` to get warranty info
    warranty_page.getinfo(serial_number)
    # ==Then== Warranty result for `serial number` is displayed
    assert warranty_page.resultheader() == serial_number
    # ==And== Verify `Warranty end date` exists in the warranty result
    assert warranty_page.resultwarranty('Warranty end date')==True
