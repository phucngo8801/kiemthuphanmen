import sys
import time
sys.path.append("G:/kiemthuphanmem3")

from pageObjects.SearchPage import SearchPage

class TestSearch():
    search = 'font-end'

    def __init__(self, driver):
        self.driver = driver

    def test_search(self):
        search = SearchPage(self.driver)
        search.click_alow()
        time.sleep(2)
        search = SearchPage(self.driver)
        search.set_search(self.search)
        time.sleep(2)
       
        search = SearchPage(self.driver)
        search.click_search()
        time.sleep(2)



        # self.driver.close()