
class SearchPage ():
    click_button_no_xpath = '//*[@id="topcv-popover-allow-button"]'
    search_xpath = '//*[@id="keyword"]'
  
    search_button_xpath = '//*[@id="frm-search-job"]/div/div[5]/button'

    def __init__(self, driver):
        self.driver = driver
    def click_alow(self):
        self.driver.find_element_by_xpath(self.click_button_no_xpath).click()

    def set_search(self, search):
        self.driver.find_element_by_xpath(self.search_xpath).send_keys(search)
   
    def click_search(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()