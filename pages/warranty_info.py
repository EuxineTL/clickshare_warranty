from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class WarrantyPage:
    URL='https://www.barco.com/en/clickshare/support/warranty-info'
    
    # Locators
    GETINFO_INPUT = (By.ID, 'SerialNumber')
    RESULT_HEADER = (By.CLASS_NAME, 'c-warranty__number')
    RESULT_WARRANTY = (By.CLASS_NAME, 'c-result-tile__dl')

    # initializer
    def __init__(self, browser):
        self.browser=browser

    # Interactions

    def load(self):
        self.browser.get(self.URL)
    
    def getinfo(self, serial_number):
        getinfo_input = self.browser.find_element(*self.GETINFO_INPUT)
        getinfo_input.send_keys(serial_number + Keys.RETURN)

    def resultheader(self):
        #result_header = self.browser.find_element(*self.RESULT_HADER)
        #return result_header.get_attribute("innerHTML")
        result_header = WebDriverWait(self.browser, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='c-result-tile__title']/.//span[contains(@class,'c-warranty__number')]")))
        return result_header.text

    def resultwarranty(self,warrany_phrase):
        result_warranty = self.browser.find_element(*self.RESULT_WARRANTY)
        return warrany_phrase in result_warranty.text
